# Animal Encyclopedia Web App

The Animal Encyclopedia Web App is a simple web application built using Flask and MongoDB that allows users to view, add, and remove information about various animals. This README file provides an overview of the application's features, how to set it up, and how to use it.

## Features

1. **Animal List**: The main page of the application displays a list of animals, including their names, descriptions, and links to Wikipedia articles about them.

2. **Add New Animals**: Users can add new animals to the database by providing a name, description, and a URL to a Wikipedia article. Upon submission, the new animal is added to the list.

3. **Remove Animals**: Users can remove animals from the database by selecting an animal from the list and clicking the "Remove" button. The selected animal will be deleted from the database.



## Pipeline Stages

1. **Checkout**: This stage checks out the source code from the Git repository.

2. **Build Docker Image**: In this stage, a Docker image is built using the specified Dockerfile (`Dockerfile`) and tagged with the name 'yoval1012/finalproject'. It also checks the Helm version inside the Docker container.

3. **Run Pytest**: This stage runs Pytest tests within a Docker container based on the previously built Docker image. It uses the `docker run` command to execute the tests contained in the `my_test.py` file.

4. **Push to Docker Hub**: After the Docker image is built and tests pass, it's pushed to Docker Hub. Docker Hub credentials are used for authentication.

5. **Build and Push Helm Chart**: This stage packages a Helm chart (located in the 'helm-chart' directory) and pushes it to a Docker registry. Docker Hub credentials are used for authentication. The Helm chart is assumed to be managed by ArgoCD.

6. **deploy with ArgoCD**: the helm chart is deploy on with argocd on default k8s cluster. 


## Getting Started

http://ip_from_argo:3001


#to kill
```
helm list
helm uninstall RELEASE_NAME
```
