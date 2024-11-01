from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy


class CustomLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        redirect_url = self.request.session.get("login_redirect_url", "")
        if redirect_url:
            del self.request.session["login_redirect_url"]
            self.request.session.modified = True
            return redirect_url
        return reverse("accounting:index")


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")

    http_method_names = ["get", "post", "options"]

    def dispatch(self, request, *args, **kwargs):
        order_pk = request.session.get("order_pk")
        login_redirect_url = request.session.get("login_redirect_url")
        response = super().dispatch(request, *args, **kwargs)
        if order_pk:
            request.session["order_pk"] = order_pk
        if login_redirect_url:
            request.session["login_redirect_url"] = login_redirect_url
        return response

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
