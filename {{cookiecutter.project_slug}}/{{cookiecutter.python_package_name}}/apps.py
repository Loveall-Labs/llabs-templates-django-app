from django.apps import AppConfig


class {{ cookiecutter.python_package_name|replace('_', ' ')|title|replace(' ', '') }}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{ cookiecutter.python_package_name }}"
