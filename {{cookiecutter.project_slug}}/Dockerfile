# syntax=docker/dockerfile:1
FROM python:3.12-bullseye

ENV PYTHONUNBUFFERED=1
WORKDIR /code

RUN python -m pip install --upgrade pip
RUN pip install tox tox-gh-actions poetry

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./{{cookiecutter.python_package_name}}/ /code/{{cookiecutter.python_package_name}}/
