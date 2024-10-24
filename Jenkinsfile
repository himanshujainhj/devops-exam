pipeline{
    agent any
    stages{
        stage("TF Init"){
            steps{
                sh 'terraform init'
            }
        }
        stage("TF Validate"){
            steps{
                sh 'terraform validate'
            }
        }
        stage("TF Plan"){
            steps{
                sh 'terraform plan'
            }
        }
        stage("TF Apply"){
            steps{
                sh 'terraform apply -auto-approve'
            }
        }

        stage('Get Subnet ID') {
            steps {
                script {
                    // Extract the subnet ID from Terraform output
                    def subnetId = sh(
                        script: "terraform output -raw subnet_id",
                        returnStdout: true
                    ).trim()
                    echo "Extracted Subnet ID: ${subnetId}"

                    // Store the subnet ID for use in the next stage
                    env.SUBNET_ID = subnetId
                }
            }
        }

        stage('Invoke Lambda') {
            steps {
                script {
                    // Create the event payload with subnet ID
                    def lambdaPayload = '{"subnet_id": "' + env.SUBNET_ID + '"}'
                    echo "Lambda Payload: ${lambdaPayload}"

                    // Invoke the Lambda function with the subnet ID in the payload
                    sh """
                    aws lambda invoke --invocation-type Event --cli-binary-format raw-in-base64-out --payload '${lambdaPayload}' --function-name my_lambda_function out --log-type Tail
                    """
                }
            }
        }
    }
}
     
