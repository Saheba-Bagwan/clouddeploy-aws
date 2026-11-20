# 🚀 CloudDeploy AWS
### Automated DevOps Deployment Platform on AWS

A hands-on DevOps project focused on application containerization, automated testing, continuous integration, and cloud deployment using Docker, GitHub Actions, and Amazon Web Services.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI/CD-2088FF?logo=githubactions&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Cloud%20Deployment-FF9900?logo=amazonaws&logoColor=white)
![Status](https://img.shields.io/badge/Project-In%20Progress-orange)

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Running the Application](#-running-the-application)
- [Docker Deployment](#-docker-deployment)
- [Continuous Integration](#-continuous-integration)
- [AWS Deployment Roadmap](#-aws-deployment-roadmap)
- [Testing](#-testing)
- [Security Considerations](#-security-considerations)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [Author](#-author)

---

## 🔍 Overview

CloudDeploy AWS is a practical DevOps engineering project designed to demonstrate the process of building, testing, containerizing, and deploying a Python web application.

The project uses Flask to develop the application, Docker to package it into a portable container, and GitHub Actions to automate application testing and Docker image builds.

The next development phase focuses on deploying the containerized application on Amazon EC2, implementing AWS identity and access management, and integrating Amazon CloudWatch for monitoring and logging.

The objective is to understand and implement a practical DevOps workflow while developing hands-on experience with Linux, Python, containerization, CI/CD, and AWS infrastructure.

**Project Status:** 🚧 In Development

---

## 🏗️ Architecture

### Current Development Architecture

```text
             Developer
                 |
                 v
          GitHub Repository
                 |
                 v
          GitHub Actions
                 |
          +------+------+
          |             |
          v             v
     Run Tests     Docker Build
          |             |
          +------+------+
                 |
                 v
          Docker Image
                 |
                 v
          Local Container
                 |
                 v
          Flask Application
```

### Planned AWS Architecture

```text
             Developer
                 |
                 v
          GitHub Repository
                 |
                 v
          GitHub Actions
                 |
            CI Pipeline
                 |
                 v
             AWS EC2
                 |
               Docker
                 |
                 v
          Flask Application
                 |
                 v
          Amazon CloudWatch
          (Monitoring & Logs)
```

*Note: The AWS architecture represents the planned implementation, not a completed deployment.*

---

## ✨ Features

### Implemented

- **Flask Web Application:** Lightweight Python web application with a homepage.
- **Health Check Endpoint:** Dedicated `/health` endpoint returning application health information.
- **Automated Unit Testing:** Python unittest framework for validating application functionality.
- **Docker Containerization:** Dockerfile for building a reproducible application image.
- **GitHub Actions Workflow:** CI configuration for automated testing and Docker image building.

### Planned

- **AWS EC2 Deployment:** Host the containerized application on an AWS virtual server.
- **AWS IAM:** Configure secure identity and access management.
- **Amazon CloudWatch:** Monitor application activity and collect logs.
- **Automated Deployment:** Extend GitHub Actions to deploy application updates to AWS.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python 3.12 |
| Backend Framework | Flask |
| Testing | Python unittest |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Version Control | Git |
| Code Hosting | GitHub |
| Development Environment | Ubuntu Linux |
| Cloud Platform | Amazon Web Services |
| Planned Compute | Amazon EC2 |
| Planned Security | AWS IAM |
| Planned Monitoring | Amazon CloudWatch |

---

## 📁 Project Structure

```text
clouddeploy-aws/
│
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI workflow
│
├── app/
│   └── app.py                  # Flask application
│
├── tests/
│   └── test_app.py             # Automated unit tests
│
├── .dockerignore               # Docker build exclusions
├── .gitignore                  # Git exclusions
├── Dockerfile                  # Docker image configuration
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🏁 Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

Make sure you have the following installed:

- Ubuntu Linux or another Linux distribution
- Python 3.12+
- pip
- Git
- Docker Engine (for containerization)

### 1. Clone the Repository

```bash
git clone https://github.com/Saheba-Bagwan/clouddeploy-aws.git
```

### 2. Navigate to the Project Directory

```bash
cd clouddeploy-aws
```

### 3. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 4. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 💡 Running the Application

Start the Flask application:

```bash
python app/app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

### Application Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Displays the application homepage |
| `/health` | GET | Returns application health information |

### Health Check

Use curl to test the health endpoint:

```bash
curl http://127.0.0.1:5000/health
```

Expected response:

```json
{
    "application": "CloudDeploy AWS",
    "status": "healthy"
}
```

---

## 🐳 Docker Deployment

The application is containerized using Docker to ensure consistent execution across different environments.

### 1. Start Docker

```bash
sudo systemctl start docker
```

### 2. Build the Docker Image

```bash
docker build -t clouddeploy-aws:latest .
```

### 3. Run the Container

```bash
docker run -d \
  --name clouddeploy-container \
  -p 127.0.0.1:5000:5000 \
  clouddeploy-aws:latest
```

### 4. Verify the Running Container

```bash
docker ps
```

### 5. Test the Containerized Application

```bash
curl http://localhost:5000/health
```

### 6. View Container Logs

```bash
docker logs clouddeploy-container
```

### 7. Stop and Remove the Container

```bash
docker rm -f clouddeploy-container
```

---

## ⚙️ Continuous Integration

GitHub Actions is used to automate the project's continuous integration workflow.

The workflow is defined in:

```text
.github/workflows/ci.yml
```

### CI Pipeline Stages

**Stage 1: Source Code Checkout**

GitHub Actions retrieves the latest repository code.

**Stage 2: Python Environment Setup**

The workflow configures Python 3.12.

**Stage 3: Dependency Installation**

Required Python packages are installed using `requirements.txt`.

**Stage 4: Automated Testing**

The workflow executes:

```bash
python -m unittest discover -s tests -v
```

**Stage 5: Docker Image Build**

After successful tests, GitHub Actions builds the Docker image:

```bash
docker build -t clouddeploy-aws:ci .
```

The workflow is configured to trigger on pushes and pull requests targeting the `main` branch.

**Verification status:** Local automated tests have passed. The GitHub-hosted workflow still needs to be executed and verified.

---

## ☁️ AWS Deployment Roadmap

The next phase focuses on deploying the containerized application to AWS.

| AWS Service | Planned Implementation |
|---|---|
| Amazon EC2 | Host the Dockerized Flask application |
| AWS IAM | Manage permissions and access securely |
| Security Groups | Configure inbound and outbound network access |
| Amazon CloudWatch | Monitor application activity and logs |

The deployment will initially be performed manually to understand the infrastructure and configuration process.

Once the application is running successfully on EC2, GitHub Actions will be extended to automate deployment.

AWS resource usage will be checked against applicable Free Tier eligibility and pricing before provisioning.

---

## 🧪 Testing

The project uses Python's built-in `unittest` framework.

Run the test suite:

```bash
python -m unittest discover -s tests -v
```

### Current Test Coverage

| Test Case | Description |
|---|---|
| Homepage response | Verifies that the homepage returns HTTP 200 |
| Health endpoint response | Verifies successful health endpoint access |
| Health response data | Validates the health status and application name |

**Current local test result:** 3 tests passed.

---

## 🔐 Security Considerations

Security is an important part of the deployment process.

The project follows these basic practices:

- Exclude sensitive files and credentials from Git.
- Avoid committing AWS access keys and private SSH keys.
- Use IAM roles and least-privilege permissions for AWS resources.
- Restrict EC2 network access using Security Groups.
- Review cloud resource costs before provisioning.

---

## 🚀 Future Enhancements

The following improvements are planned:

- [ ] Publish the project to GitHub.
- [ ] Verify the GitHub Actions CI pipeline.
- [ ] Deploy the Docker container on Amazon EC2.
- [ ] Configure AWS IAM permissions.
- [ ] Integrate Amazon CloudWatch monitoring.
- [ ] Implement automated AWS deployment through GitHub Actions.
- [ ] Improve deployment security and reliability.

---

## 👩‍💻 Author

**Saheba Bagwan**

Aspiring Cloud & DevOps Engineer | AWS | Linux | Python | Docker | CI/CD

- GitHub: [@Saheba-Bagwan](https://github.com/Saheba-Bagwan)

---

