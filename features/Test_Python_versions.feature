Feature: The versions for the containers should match correctly
    the expected values.

Scenario: Test python 2.7
Given I run the docker container for 'germaniumhq/python:2.7'
When I get the version of the default python command
Then it is version '2.7'


