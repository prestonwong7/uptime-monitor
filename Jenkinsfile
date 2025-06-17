pipeline {
    agent any
    stages {
        stage('Setup Venv') {
            steps {
                 sh 'python -m venv venv'
                // Upgrade pip inside venv
                sh './venv/bin/pip install --upgrade pip'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Monitor') {
            steps {
                sh './venv/bin/python monitor.py'
            }
        }
    }
}