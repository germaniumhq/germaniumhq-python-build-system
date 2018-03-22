from behave import use_step_matcher, step
from unittest import TestCase
import subprocess
import re

assertEqual = TestCase().assertEqual

VERSION_MATCHER = re.compile('^Python ((\d+\.\d+)\.\d+)')

use_step_matcher("re")


@step("I run the docker container for '(.*)'")
def run_docker_container(context, container_name: str) -> None:
    context.container_name = container_name


@step("I check if pip it's installed")
def run_pip_to_see_if_it_is_installed(context):
    run_docker_command(context, "which", "pip")


def run_docker_command(context, *parameters):
    program = ['docker', 'run', '-t', '--rm', context.container_name]
    program.extend(parameters)
    output = subprocess.check_output(program) # type: bytes
    context.docker_output = output.decode('utf-8').strip()


@step("it's instaled in the container in /python")
def check_pip_version_name(context):
    assertEqual(context.docker_output, "/python/bin/pip")


@step("I get the version of the default python command")
def get_python_version(context) -> None:
    run_docker_command(context, "python", "--version")


@step("it is version '(.*)'")
def check_python_version(context, container_name: str) -> None:
    m = VERSION_MATCHER.match(context.docker_output)
    if not m:
        raise Exception("Unable to parse version from: %s" % context.docker_output)

    context.python_version = m.group(2)

    assertEqual(container_name, context.python_version)
