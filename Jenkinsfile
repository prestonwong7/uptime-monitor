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
        stage('Run Uptime Monitor') {
            steps {
                script {
                    // Run the uptime monitor script
                    bat 'venv\\Scripts\\python.exe monitor.py'
                }
            }
        }

    }
}