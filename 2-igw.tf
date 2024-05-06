resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.ntconsult.id

  tags = {
    Name = "igw"
  }
}
