pipeline {
    agent any
    stages {
        stage('Virtual Environment') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                    // Activate the virtual environment
                    sh '. venv/bin/activate'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies from requirements.txt
                    sh 'venv/bin/pip install -r requirements.txt'
                }
            }
        }
        stage('Run Uptime Monitor') {
            steps {
                script {
                    // Run the uptime monitor script
                    sh 'venv/bin/python uptime_monitor.py'
                }
            }
        }

    }
}