def awsCredentials = [[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'AWS_Credentials']]

pipeline {
    agent any
    stages{
        stage('Deploy') {
            steps {
                bat "cdk bootstrap aws://592715633892/eu-west-1"
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