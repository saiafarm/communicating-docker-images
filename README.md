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
```

### 2. Deploy to Kubernetes:
Apply the Kubernetes configurations:
```bash
kubectl apply -f kubernetes/
```

### 3. Verify Deployment:
Check that the pods are running:
```bash
kubectl get pods
```

## Testing:
### Access Flask Pod:
```bash
kubectl exec -it <flask-pod-name> -- /bin/bash
```

### Test Flask Endpoint:
```bash
python -c "import requests; response = requests.get('http://localhost:5000/hello'); print(response.text)"
```

### Test Spring Boot Endpoint via Flask:
```
python -c "import requests; response = requests.get('http://localhost:5000/spring-hello'); print(response.text)"
```
Replace <flask-pod-name> with your actual Flask pod's name which can be retrieved using kubectl get pods.


This README provides instructions for setting up and testing intercommunication between Flask and Spring Boot servers in a Kubernetes environment. Adjust paths and commands according to your project structure and Kubernetes setup.



