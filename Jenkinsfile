stage('Create Run Containers') {
    def parallelJobs = [:]

    parallelJobs."Python 2.7" = {
        node {
            deleteDir()
            checkout scm

            docker.build('germaniumhq/python:2.7',
                         'python-2.7')
        }
    }

    parallelJobs."Python 3.4" = {
        node {
            deleteDir()
            checkout scm

            docker.build('germaniumhq/python:3.4',
                         'python-3.4')
        }
    }

    parallelJobs."Python 3.5" = {
        node {
            deleteDir()
            checkout scm

            docker.build('germaniumhq/python:3.5',
                         'python-3.5')
        }
    }

    parallelJobs."Python 3.6" = {
        node {
            deleteDir()
            checkout scm

            docker.build('germaniumhq/python:3.6',
                         'python-3.6')
        }
    }

    parallelJobs."Python 3.6 (Alpine)" = {
        node {
            deleteDir()
            checkout scm

            docker.build('germaniumhq/python-alpine:3.6',
                         'python-alpine-3.6-build')
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

            docker.build('germaniumhq/python-build:2.7',
                         'python-2.7-build')
        }
    }

    jobs."Python 3.4 Build" = {
        node {
            deleteDir()
            checkout scm

            docker.build('germaniumhq/python-build:3.4',
                         'python-3.4-build')
        }
    }

    jobs."Python 3.5 Build" = {
        node {
            deleteDir()
            checkout scm

            docker.build('germaniumhq/python-build:3.5',
                         'python-3.5-build')
        }
    }

    jobs."Python 3.6 Build" = {
        node {
            deleteDir()
            checkout scm

            docker.build('germaniumhq/python-build:3.6',
                         'python-3.6-build')
        }
    }

    jobs."Python 3.6 Child Build" = {
        node {
            deleteDir()
            checkout scm

            docker.build('germaniumhq/python-build-child:3.6',
                         'python-build-child-3.6')
        }
    }

    parallel(jobs)
}

