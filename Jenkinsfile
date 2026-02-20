pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pip3 show pytest || pip3 install pytest'
                sh 'python3 -m pytest test_app.py -v'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python3 app.py &'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed! Check the logs!'
        }
    }
}
