pipeline {
    agent any
    stages{
        stage('Deploy') {
            steps {
                sh 'cdk deploy --require-approval=never'
            }
        }

        stage('Destroy') {
            steps {
                sh 'cdk destroy --require-approval=never'
            }
        } 
    }
}