from typing import Any

from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.urls import reverse


class CustomLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self) -> str:
        redirect_url: str = self.request.session.get("login_redirect_url", "")
        if redirect_url:
            del self.request.session["login_redirect_url"]
            self.request.session.modified = True
            return redirect_url
        return reverse("accounting:index")


class CustomLogoutView(LogoutView):
    next_page: str = "login"

    http_method_names = ["get", "post", "options"]

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        order_pk = request.session.get("order_pk")
        login_redirect_url = request.session.get("login_redirect_url")
        response = super().dispatch(request, *args, **kwargs)
        if order_pk:
            request.session["order_pk"] = order_pk
        if login_redirect_url:
            request.session["login_redirect_url"] = login_redirect_url
        return response

    def get(self, *args: Any, **kwargs: Any) -> HttpResponse:
        return self.post(*args, **kwargs)
