pipeline {
    agent any
    stages {
        stage('Setup Venv') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate.bat
                pip install --upgrade pip
                '''
            }
        }
        stage('Install Dependencies') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Monitor') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                python monitor.py
                '''
            }
        }
    }
}