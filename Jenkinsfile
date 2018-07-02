def baseImages = [
    "germaniumhq/python:2.7": "python-2.7",
    "germaniumhq/python:3.4": "python-3.4",
    "germaniumhq/python:3.5": "python-3.5",
    "germaniumhq/python:3.6": "python-3.6",
    "germaniumhq/python-alpine:3.6": "python-alpine-3.6-build"
]

def runImages = [
    "germaniumhq/python-build:2.7": "python-2.7-build",
    "germaniumhq/python-build:3.4": "python-3.4-build",
    "germaniumhq/python-build:3.5": "python-3.5-build",
    "germaniumhq/python-build:3.6": "python-3.6-build",
    "germaniumhq/python-build-child:2.7": "python-build-child-2.7",
    "germaniumhq/python-build-child:3.4": "python-build-child-3.4",
    "germaniumhq/python-build-child:3.5": "python-build-child-3.5",
    "germaniumhq/python-build-child:3.6": "python-build-child-3.6",
]

germaniumBuildSystemPipeline(
    baseImages: baseImages,
    runImages: runImages)
