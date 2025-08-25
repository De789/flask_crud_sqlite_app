pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/De789/flask_crud_sqlite_app.git'
            }
        }

        // stage('Build Docker Image') {
        //     steps {
        //         script {
        //             docker.build("flask_crud_sqlite_app:latest")
        //         }
        //     }
        // }

        // stage('Run Container') {
        //     steps {
        //         script {
        //             docker.image("flask_crud_sqlite_app:latest").run('-p 5000:5000')
        //         }
        //     }
        // }
    }
}
