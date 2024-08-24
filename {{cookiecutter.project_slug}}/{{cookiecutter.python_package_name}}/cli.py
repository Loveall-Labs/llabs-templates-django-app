"""Console script for {{cookiecutter.python_package_name}}."""

{% if cookiecutter.command_line_interface|lower == 'fire' -%}
import fire


def help() -> None:
    print("{{ cookiecutter.python_package_name }}")
    print("=" * len("{{ cookiecutter.python_package_name }}"))
    print("{{ cookiecutter.project_short_description }}")

def main() -> None:
    fire.Fire({
        "help": help
    })


if __name__ == "__main__":
    main() # pragma: no cover
{%- endif %}
