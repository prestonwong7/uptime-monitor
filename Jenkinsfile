pipeline {
    agent any
    stages {
        stage('Virtual Environment') {
            steps {
                script {
                    // Create a virtual environment
                    bat 'python3 -m venv venv'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies from requirements.txt
                    bat 'venv\Scripts\pip.exe install -r requirements.txt'
                }
            }
        }
        stage('Run Uptime Monitor') {
            steps {
                script {
                    // Run the uptime monitor script
                    bat 'venv\\Scripts\\python.exe uptime_monitor.py'
                }
            }
        }

    }
}