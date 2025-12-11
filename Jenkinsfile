pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['ec2-key']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no ubuntu@3.111.34.88 "
                            cd /home/ubuntu/backend;

                            echo 'Pulling latest code...';
                            git pull;

                            echo 'Setting up virtual environment...';
                            if [ ! -d venv ]; then
                                python3 -m venv venv;
                            fi
                            source venv/bin/activate;

                            echo 'Installing dependencies...';
                            pip install -r requirements.txt;

                            echo 'Restarting Gunicorn...';
                            pkill gunicorn || true;

                            nohup gunicorn -w 4 -b 0.0.0.0:5000 app:app > gunicorn.log 2>&1 &
                        "
                    '''
                }
            }
        }
    }
}
