pipeline {
    agent any
    stages {
        stage('Setup Venv') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\pip.exe install --upgrade pip
                '''
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt'
            }
        }
        stage('Run Monitor') {
            steps {
                bat 'venv\\Scripts\\python.exe monitor.py'
            }
        }
    }
}
