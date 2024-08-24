#!/bin/bash

# Uncomment the following to config github secret used by github workflow.
gh secret set PERSONAL_TOKEN --body $GH_TOKEN
gh secret set PYPI_API_TOKEN --body $PYPI_API_TOKEN
gh secret set TEST_PYPI_API_TOKEN --body $TEST_PYPI_API_TOKEN
