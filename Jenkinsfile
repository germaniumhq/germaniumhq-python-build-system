stage('Build Run Containers') {
    def parallelJobs = [:]

    parallelJobs."Python 2.7" = {
        node {
            deleteDir()

            checkout scm

            dockerBuild file: 'python-2.7/Dockerfile',
                tags: ['germaniumhq/python:2.7']
        }
    }

    parallel(parallelJobs)
}

