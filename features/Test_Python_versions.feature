Feature: The versions for the containers should match correctly
    the expected values.

Scenario: Test python 2.7
Given I run the docker container for 'germaniumhq/python:2.7'
When I get the version of the default python command
Then it is version '2.7'
When I check if pip it's installed
Then it's instaled in the container in /python

Scenario: Test python 3.4
Given I run the docker container for 'germaniumhq/python:3.4'
When I get the version of the default python command
Then it is version '3.4'
When I check if pip it's installed
Then it's instaled in the container in /python

Scenario: Test python 3.5
Given I run the docker container for 'germaniumhq/python:3.5'
When I get the version of the default python command
Then it is version '3.5'
When I check if pip it's installed
Then it's instaled in the container in /python

Scenario: Test python 3.6
Given I run the docker container for 'germaniumhq/python:3.6'
When I get the version of the default python command
Then it is version '3.6'
When I check if pip it's installed
Then it's instaled in the container in /python
