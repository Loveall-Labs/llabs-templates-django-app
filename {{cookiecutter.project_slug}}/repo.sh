#!/bin/bash
# TODO: Rework file to use Cruft

# !!!NOTICE!!
# Personal token with full access rights is required to run this scripts
# Once you got persona token, set enviroment variable GH_TOKEN with it

# Create repo and push code to github
gh repo create {{cookiecutter.project_slug}} --public
git remote add origin git@github.com:Loveall-Labs/{{cookiecutter.project_slug}}.git
git add .
pre-commit run --all-files
git add .
git commit -m "Initial commit by ppw"
git branch -M main

# Config github secret used by github workflow.
gh secret set PERSONAL_TOKEN --body $GH_TOKEN
gh secret set PYPI_API_TOKEN --body $PYPI_API_TOKEN
gh secret set TEST_PYPI_API_TOKEN --body $TEST_PYPI_API_TOKEN

git push -u origin main
