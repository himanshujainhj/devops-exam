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
        // stage("TF Apply"){
        //     steps{
        //         sh 'terraform apply -auto-approve'
        //     }
        // }
        // stage("Invoke Lambda"){
        //     steps {
        //         script {
        //             def lambdaResult = sh(
        //                 script: "aws lambda invoke --function-name my_lambda_function --log-type Tail output.log",
        //                 returnStdout: true
        //             ).trim()
        //             echo "Lambda Invocation Result: ${lambdaResult}"
        //         }
        //     }
        // }
    }
}

