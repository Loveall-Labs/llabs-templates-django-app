#!/usr/bin/env python
import asyncio
import functools
import os
import shlex
import sys

import colorama
from colorama import Fore, Style

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


async def _echo(stream):
    while True:
        line = await stream.readline()
        line = line.decode("utf-8")
        if not line:
            break
        line = line.rstrip("\n")
        if line.upper().startswith("WARNING"):
            print(Fore.YELLOW + line + Style.RESET_ALL)
        elif line.upper().startswith("ERROR"):
            print(Fore.RED, line, Style.RESET_ALL)
            raise Exception(line)
        else:
            print(line)


def async_run(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return asyncio.run(func(*args, **kwargs))

    return wrapper


async def aioprocess(
    *cmds,
    stdout_handler=_echo,
    stderr_handler=_echo,
    inherit_env=True,
    detached=False,
    cwd=None,
):
    """execute cmds in asyncio process, and echo it's stdout/stderr

    if detached is specified, the subprocess will be detached with parent after created.
    if inherit_env is specified, then subprocess with inherite envars from parent process.

    Args:
        *cmds: list of cmds to be executed
        stdout_handler: handler for stdout
        stderr_handler: handler for stderr
        inherit_env: inherit envars from parent process
        detached: detach subprocess with parent
        cwd: change working directory of subprocess
    Examples:
        >>> aioprocess("ls")
        >>> aioprocess("ping -c 10 www.baidu.com")
        >>> aioprocess("ping", "-c", "10", "www.baidu.com")
        >>> aioprocess("python -m http.server", detached=True)
    """
    cur_dir = os.getcwd()

    try:
        if cwd:
            os.chdir(cwd)

        if len(cmds) == 1 and isinstance(cmds[0], str):
            cmds = shlex.split(cmds[0])

        env = os.environ.copy() if inherit_env else None

        proc = await asyncio.create_subprocess_exec(
            *cmds,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            start_new_session=detached,
            env=env,
        )

        if stdout_handler:
            asyncio.ensure_future(stdout_handler(proc.stdout))
        if stderr_handler:
            asyncio.ensure_future(stderr_handler(proc.stderr))

        return proc
    finally:
        os.chdir(cur_dir)


# @async_run
# async def main():
#     try:
#         proc = await aioprocess("pip install tqdm")
#         await proc.wait()
#     except Exception as e:
#         print("ecxeption:", e)

# main()


def remove_file(filepath):
    try:
        os.remove(os.path.join(PROJECT_DIRECTORY, filepath))
    except FileNotFoundError:
        pass


@async_run
async def execute(*args, cwd=None):
    cur_dir = os.getcwd()

    proc = await aioprocess(*args, cwd=cwd)
    await proc.wait()


def init_git():
    if not os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
        execute("git", "init", cwd=PROJECT_DIRECTORY)
        execute(
            "git",
            "config",
            "user.name",
            "{{ cookiecutter.full_name }}",
            cwd=PROJECT_DIRECTORY,
        )
        execute(
            "git",
            "config",
            "user.email",
            "{{ cookiecutter.email }}",
            cwd=PROJECT_DIRECTORY,
        )


def init_dev():
    print(Style.NORMAL, Fore.BLUE, "installing pre-commit hooks...")
    print(Style.RESET_ALL, Style.DIM)
    try:
        execute(sys.executable, "-m", "pip", "install", "pre-commit")
        execute("pre-commit", "install", cwd="{{ cookiecutter.project_slug }}")
        print(Style.NORMAL, Fore.GREEN, "pre-commit hooks was successfully installed")
        print(Style.RESET_ALL)
    except Exception as e:
        print(e)
        print(
            Fore.YELLOW,
            "failed to install pre-commit hooks. You may need run `pre-commit install` later by your self",
            Style.RESET_ALL,
        )

    print(Style.NORMAL, Fore.BLUE, "installing poetry...")
    print(Style.RESET_ALL, Style.DIM)

    try:
        execute(sys.executable, "-m", "pip", "install", "poetry")
        print(Style.NORMAL, Fore.GREEN, "poetry installed successfully", Style.RESET_ALL)
    except Exception as e:
        print(e)
        print(
            Fore.YELLOW,
            "failed to install poetry, you may need re-run the task by yourself.",
            Style.RESET_ALL,
        )
        return

    try:
        print(Style.NORMAL, Fore.BLUE, "install all dev dependency packages...")
        print(Style.RESET_ALL, Style.DIM)
        execute("poetry", "install", "-E", "dev", "-E", "doc", "-E", "test", cwd=PROJECT_DIRECTORY)
        print(
            Style.NORMAL,
            Fore.GREEN,
            "all dev dependency packages installed successfully",
            Style.RESET_ALL,
        )
    except Exception as e:
        print(e)
        print(
            Style.NORMAL,
            Fore.YELLOW,
            "failed to install dev dependency packages, you may need re-run the task by yourself: poetry install -E dev -E test -E doc",
            Style.RESET_ALL,
        )


if __name__ == "__main__":
    colorama.init()

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.md")
        remove_file("docs/authors.md")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.project_slug }}", "cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    try:
        init_git()
    except Exception as e:
        print(e)

    if "{{ cookiecutter.init_dev_env }}" == "y":
        try:
            init_dev()
        except Exception as e:
            print(e)
