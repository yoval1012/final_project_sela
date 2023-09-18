pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from your version control system (e.g., Git)
                checkout scm
            }
        }
        stage('Build and Publish Docker Image') {
            agent {
                docker {
                    image 'docker:20.10' // Specify the Docker image version you need
                    args '-v /var/run/docker.sock:/var/run/docker.sock' // Mount the Docker socket into the container
                }
            }

        stage('Build Docker Image with Helm') {
            steps {
                // Build your Docker image with Helm chart using a Dockerfile
                script {
                    def dockerImage = docker.build('app:latest', '.') // Build Docker image with your Helm chart

                    // Optionally, you can install Helm and other dependencies in the Docker image if needed.
                    dockerImage.inside {
                        sh 'helm version' // Example: Run Helm commands inside the Docker image
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                // Push the Docker image to Docker Hub
                script {
                    withCredentials([usernamePassword(credentialsId: 'dckr_pat_6M1dtPndQqDUOUSA5mxFR1zMA9I', usernameVariable: 'yoval1012', passwordVariable: '@VD#26-6nFNyH*y')]) {
                        def dockerHubImage = "yoval1012/finalproject:app"
                        docker.withRegistry('https://registry.hub.docker.com', 'dockerHubCredentials') {
                            dockerImage.push()
                            dockerImage.push("${dockerHubImage}")
                        }
                    }
                }
            }
        }
    }

}    



