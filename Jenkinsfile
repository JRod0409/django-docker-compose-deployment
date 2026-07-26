pipeline {
    agent any

    environment {
        SECRET_KEY = 'jenkins-ci-secret-key-for-testing'
    }

    stages {
        stage('Checkout') {
            steps {
                // Replace with YOUR actual GitHub repository URL
                git branch: 'main', url: 'https://github.com/JRod0409/django-docker-compose-deployment.git'
            }
        }

        stage('Lint & Static Checks') {
            steps {
                // Runs flake8 linting inside the container
                sh 'docker compose run --rm app sh -c "flake8"'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Runs Django unit tests
                sh 'docker compose run --rm app sh -c "python manage.py test"'
            }
        }

        stage('Build & Deploy') {
            steps {
                // Tear down existing containers and launch detached updated stack
                sh 'docker compose down'
                sh 'docker compose up --build -d'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}