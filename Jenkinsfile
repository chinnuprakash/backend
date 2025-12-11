pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo "Building your project..."
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying to server..."
            }
        }
    }
}
