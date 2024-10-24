# Create a Private Subnet
resource "aws_subnet" "private_subnet" {
  vpc_id            = data.aws_vpc.vpc.id
  cidr_block        = "10.0.1.0/24" 
  availability_zone = "ap-south-1a"
  map_public_ip_on_launch = false
  tags = {
    Name = "private-subnet"
  }
}

# Route Table for the Subnet
resource "aws_route_table" "private_route_table" {
  vpc_id = data.aws_vpc.vpc.id

  route {
    nat_gateway_id = data.aws_nat_gateway.nat.id
    destination_cidr_block = "0.0.0.0/0"
  }

  tags = {
    Name = "private-route-table"
  }
}

resource "aws_route_table_association" "subnet_association" {
  subnet_id      = aws_subnet.private_subnet.id
  route_table_id = aws_route_table.private_route_table.id
}

# Security Group for Lambda
resource "aws_security_group" "lambda_sg" {
  vpc_id = data.aws_vpc.exam_vpc.id

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "lambda-sg"
  }
}