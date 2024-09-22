# syntax=docker/dockerfile:1
FROM python:3.12-bullseye

ENV PYTHONUNBUFFERED=1
WORKDIR /code

RUN python -m pip install --upgrade pip
RUN pip install tox tox-gh-actions poetry

RUN poetry config virtualenvs.create false

COPY README.md /code/
COPY pyproject.toml /code/
RUN poetry install --only local_dev --no-root
