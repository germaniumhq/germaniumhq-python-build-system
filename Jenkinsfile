stage('Create Run Containers') {
    def parallelJobs = [:]

    parallelJobs."Python 2.7" = {
        node {
            deleteDir()

            checkout scm

            dockerBuild file: 'python-2.7/Dockerfile',
                tags: ['germaniumhq/python:2.7']
        }
    }

    parallelJobs."Python 3.4" = {
        node {
            deleteDir()

            checkout scm

            dockerBuild file: 'python-3.4/Dockerfile',
                tags: ['germaniumhq/python:3.4']
        }
    }

    parallelJobs."Python 3.5" = {
        node {
            deleteDir()

            checkout scm

            dockerBuild file: 'python-3.5/Dockerfile',
                tags: ['germaniumhq/python:3.5']
        }
    }

    parallelJobs."Python 3.6" = {
        node {
            deleteDir()

            checkout scm

            dockerBuild file: 'python-3.6/Dockerfile',
                tags: ['germaniumhq/python:3.6']
        }
    }

    parallel(parallelJobs)
}

stage('Create Build Containers') {
    def jobs = [:]

    jobs."Python 2.7 Build" = {
        node {
            deleteDir()

            checkout scm

            dockerBuild file: 'python-2.7-build/Dockerfile',
                tags: ['germaniumhq/python-build:2.7']
        }
    }

    jobs."Python 3.6 Build" = {
        node {
            deleteDir()

            checkout scm

            dockerBuild file: 'python-3.6-build/Dockerfile',
                tags: ['germaniumhq/python-build:3.6']
        }
    }

    parallel(jobs)
}
