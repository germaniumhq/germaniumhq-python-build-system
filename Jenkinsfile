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
    "germaniumhq/python-build-child:3.6": "python-build-child-3.6",
]

def runDockerBuild = { imageName, folderName ->
    node {
        deleteDir()
        checkout scm

        docker.build(imageName, folderName)
    }
}

def runDockerPush = { imageName, folderName ->
    node {
        dpush imageName
    }
}

def runParallelBuilds = { imageMap, code ->
    def parallelJobs = [:]

    imageMap.entrySet().each({e ->
        def image = e.key
        def folder = e.value

        parallelJobs[image] = {
            code(image, folder)
        }
    })

    parallel(parallelJobs)
}

stage('Create Base/Run Containers') {
    runParallelBuilds(baseImages, runDockerBuild)
}

stage('Create Build Containers') {
    runParallelBuilds(runImages, runDockerBuild)
}

stage('Push docker containers') {
    def allImages = [:]
    allImages.putAll(baseImages)
    allImages.putAll(runImages)

    runParallelBuilds(allImages, runDockerPush)
}
