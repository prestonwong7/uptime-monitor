pipeline {
    agent any
    stages {
        stage('Setup Venv') {
            steps {
                bat 'python -m venv venv'
            }
        }
        stage('Check Workspace Files') {
            steps {
                bat 'dir'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
            }
        }
        stage('Check Venv Scripts') {
            steps {
                bat 'dir venv\\Scripts'
            }
        }
        stage('Run Monitor') {
            steps {
                bat 'venv\\Scripts\\python.exe monitor.py'
            }
        }
    }
}