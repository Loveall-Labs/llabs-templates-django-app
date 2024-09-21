# Contributing

## Report Bugs

Report bugs at https://github.com/Loveall-Labs/{{ cookiecutter.project_slug }}/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

## Get Started!

Ready to contribute? Here's how to set up `{{ cookiecutter.project_slug }}` for local development.

1. Clone the repo locally
    ```
        $ git clone git@github.com:Loveall-Labs/{{ cookiecutter.project_slug }}.git
    ```
2. Ensure [poetry](https://python-poetry.org/docs/) is installed.
3. Install dependencies and start your virtualenv:
    ```
        $ poetry install -E test -E doc -E dev
    ```
4. Create a branch for local development:
    ```
        $ git checkout -b name-of-your-bugfix-or-feature
    ```

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass the
   tests, including testing other Python versions, with tox:

    ```
        $ tox
    ```

6. Commit your changes and push your branch to GitHub:

    ```
        $ git add .
        $ git commit -m "Your detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature
    ```

7. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.
3. The pull request should work for Python 3.8, 3.9, 3.10, 3.11, 3.12 and for PyPy. Check
   https://github.com/Loveall-Labs/{{ cookiecutter.project_slug }}/actions
   and make sure that the tests pass for all supported Python versions.

## Tips

```
    $ pytest tests.test_{{ cookiecutter.project_slug }}
```
To run a subset of tests.


## Deploying

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.md).
Then run:

```
$ poetry patch # possible: major / minor / patch
$ git push
$ git push --tags
```

Github Actions will then deploy to PyPI if tests pass.
