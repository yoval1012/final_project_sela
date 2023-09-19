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
                // Checkout your source code from your version control system (e.g., Git)
                checkout scm
            }
        }
        
       // stage('Install Helm') {
         //   steps {
           //     sh 'curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash'
            //}
        //}

        stage('Build Docker Image with Helm') {
            steps {
            // Build your Docker image with Helm chart using a Dockerfile
                script {
                    def dockerImage = docker.build('app:latest', '-f Dockerfile .') // Build Docker image with your Helm chart

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
                    def dockerImage = docker.image('app:latest')
                    docker.withRegistry('https://hub.docker.com/repository/docker/yoval1012/finalproject', 'yuvals_dockerhub') {
                        dockerImage.push()
                        dockerImage.push("${DOCKERHUB_IMAGE}")
                    }
                }
            }
        }
    }
}




