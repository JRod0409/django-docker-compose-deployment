pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/henry-books.git'
            }
        }

        stage('Lint & Static Checks') {
            steps {
                sh 'docker-compose run --rm app sh -c "flake8"'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'docker-compose run --rm app sh -c "python manage.py test"'
            }
        }

        stage('Build & Deploy') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up --build -d'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}