from behave import use_step_matcher, step
from unittest import TestCase
import subprocess
import re

assertEqual = TestCase().assertEqual
VERSION_MATCHER = re.compile('^Python ((\d+\.\d+)\.\d+)')

use_step_matcher("re")


@step("I run the docker container for '(.*)'")
def run_docker_container(context, container_name: str) -> None:
    output = subprocess.check_output(['docker', 'run', '-t', '--rm', container_name, 'python', '--version']) # type: bytes
    context.docker_output = output.decode('utf-8')
    

@step("I get the version of the default python command")
def get_python_version(context) -> None:
    m = VERSION_MATCHER.match(context.docker_output)
    if not m:
        raise Exception("Unable to parse version from: %s" % context.docker_output)

    context.python_version = m.group(2)


@step("it is version '(.*)'")
def check_python_version(context, container_name: str) -> None:
    assertEqual(container_name, context.python_version)
