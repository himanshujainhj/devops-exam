resource "aws_lambda_function" "my_lambda" {
  filename         = "lambda_payload.zip"  # Your Lambda code ZIP
  function_name    = "my_lambda_function"
  role             = data.aws_iam_role.lambda.arn
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.9"

  vpc_config {
    subnet_ids         = [aws_subnet.private_subnet.id]
    security_group_ids = [aws_security_group.lambda_sg.id]
  }
}
