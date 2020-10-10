def awsCredentials = [[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'AWS_Credentials']]

pipeline {
    agent any
    stages{
        stage('Deploy') {
            steps {
                bat "cdk --version"
                bat "cdk deploy --require-approval=never"
            }
        }

        stage('Destroy') {
            steps {
                bat "cdk destroy --require-approval=never"
            }
        } 
    }
}