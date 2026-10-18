pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        disableConcurrentBuilds()
        timeout(time: 15, unit: 'MINUTES')
    }

    environment {
        STUDENT_NAME = 'Oybek'
        STUDENT_SURNAME = 'Yuldashov'
        STUDENT_GROUP = 'IT2-2307'
        STUDENT_ID = '41559'
        IMAGE_NAME = 'yuldashov-oybek-devops'
        CONTAINER_NAME = 'yuldashov-oybek-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log -1 --oneline'
                echo "Student: ${env.STUDENT_NAME} ${env.STUDENT_SURNAME}"
                echo "Group: ${env.STUDENT_GROUP}, ID: ${env.STUDENT_ID}"
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m compileall app'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s tests -v'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t "$IMAGE_NAME" .'
                sh 'docker images "$IMAGE_NAME"'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker info > /dev/null
                    if [ -n "$(docker ps -aq --filter "name=^/${CONTAINER_NAME}$")" ]; then
                        docker rm -f "$CONTAINER_NAME"
                    fi
                    docker run -d --init --name "$CONTAINER_NAME" \
                        -p 127.0.0.1:8000:8000 \
                        -e STUDENT_NAME \
                        -e STUDENT_SURNAME \
                        -e STUDENT_GROUP \
                        -e STUDENT_ID \
                        "$IMAGE_NAME"
                '''
                retry(5) {
                    sleep(time: 2, unit: 'SECONDS')
                    sh '''
                        docker exec "$CONTAINER_NAME" python -c 'import urllib.request; r = urllib.request.urlopen("http://127.0.0.1:8000", timeout=5); text = r.read().decode(); print(text); assert r.status == 200; assert "Student ID: 41559" in text'
                    '''
                }
                sh 'docker ps --filter "name=^/${CONTAINER_NAME}$"'
                sh 'docker logs "$CONTAINER_NAME"'
            }
        }
    }
}
