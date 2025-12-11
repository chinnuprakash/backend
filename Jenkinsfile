pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    cd backend
                    python3 -m venv venv || true
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['ec2-key']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no ubuntu@3.111.34.88 "
                        cd /home/ubuntu/backend;
                        git pull;
                        source venv/bin/activate;
                        pip install -r requirements.txt;
                        pkill gunicorn || true;
                        nohup gunicorn -w 4 -b 0.0.0.0:5000 app:app > gunicorn.log 2>&1 &
                        "
                    '''
                }
            }
        }
    }
}
