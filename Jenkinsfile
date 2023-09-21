pipeline {
    agent {
        kubernetes {
            label 'slave'
            yamlFile 'build-pod.yaml'
            defaultContainer 'ez-docker-helm-build'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build('yoval1012/finalproject', '-f Dockerfile .')
                    dockerImage.inside {
                        sh 'helm version'
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    def dockerImage = docker.image('yoval1012/finalproject')
                    docker.withRegistry('https://registry.hub.docker.com', 'yuval_dockerhub') {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Run Pytest') {
            steps {
                script {
                    try {
                        def customDockerImage = docker.image('yoval1012/finalproject')
                        //customDockerImage.inside {
                            // Assuming your pytest command is something like this
                        sh 'docker run yoval1012/finalproject:latest app/test_syntax.py' 
                        //}
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error("Failed to run pytest: ${e.message}")
                    }
                }
            }
        }
    }
}
