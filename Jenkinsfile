pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Hari-haran1788/python-jenkins.git'
            }
        }

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
