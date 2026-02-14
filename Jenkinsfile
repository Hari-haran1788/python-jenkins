pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t django-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8000:8000 django-app'
            }
        }

        stage('Test') {
            steps {
                sh 'curl localhost:8000'
            }
        }
    }
}
