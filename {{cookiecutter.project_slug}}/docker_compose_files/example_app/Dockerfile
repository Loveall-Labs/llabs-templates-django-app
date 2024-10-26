# syntax=docker/dockerfile:1
FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/root/.local/bin:/app/.venv/bin:$PATH"

WORKDIR /code/example_app

# Install Poetry
RUN apt-get update \
    && apt-get install -y curl pipx python3-venv \
    && pipx install poetry \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install example app dependencies
COPY pyproject.toml poetry.lock /code/
RUN poetry install --no-interaction --no-ansi --with example_app

# Install example_app and library as editable apps (so we don't have to re-install them every time we edit a file.
RUN poetry add --editable /code/example_app --editable /code/{{cookiecutter.python_package_name}}
