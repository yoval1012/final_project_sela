pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from your version control system (e.g., Git)
                checkout scm
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



