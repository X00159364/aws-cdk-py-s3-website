def awsCredentials = [[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'AWS_Credentials']]

pipeline {
    agent any
    stages{
        stage('Deploy') {
            steps {
                bat'npm install -g aws-cdk'
                bat 'cdk deploy --require-approval=never'
            }
        }

        stage('Destroy') {
            steps {
                bat 'cdk destroy --require-approval=never'
            }
        } 
    }
}