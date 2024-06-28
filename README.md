# Flask and Spring Boot Docker Communication

This code demonstrates the communication between a Flask server and a Spring Boot server, each running in its own Docker container within a Kubernetes cluster. The Flask server forwards requests to the Spring Boot server and serves its own endpoint.

## Prerequisites:
- Docker
- Kubernetes (Minikube or any Kubernetes cluster)
- kubectl

## Repository Structure:
- `/flask-app`: Contains the Flask application and Dockerfile.
- `/spring-boot-app`: Contains the Spring Boot application and Dockerfile.
- `/kubernetes`: Contains all Kubernetes deployment and service YAML files.

## Setup Instructions:

### 1. Build Docker Images:
Navigate to each application directory and build the Docker images:
```bash
docker build -t flask-app ./flask-app
docker build -t spring-boot-app ./spring-boot-app
