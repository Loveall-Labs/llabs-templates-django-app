# syntax=docker/dockerfile:1
FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH="/root/.local/bin:$PATH"

WORKDIR /code

# Install Poetry
RUN apt-get update \
    && apt-get install -y curl pipx python3-venv \
    && pipx install poetry \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install library, example app, & dependencies
COPY pyproject.toml README.md /code/
COPY {{cookiecutter.python_package_name}}/* /code/{{cookiecutter.python_package_name}}/
COPY example_app /code/example_app
RUN poetry lock --no-interaction && poetry install --no-interaction --no-ansi --with example_app

# Set this path to within the example app to make manage.py make sense.
WORKDIR /code/example_app/example_app/

# Use entrypoint to activcate Poetry venv (that poetry installed everything to above) before executing other things
ENTRYPOINT ["/bin/bash", "-c", "source /code/.venv/bin/activate && exec \"$@\"", "--"]
