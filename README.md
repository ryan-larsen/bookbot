# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EC2Inventory",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeTags",
                "ec2:DescribeAvailabilityZones",
                "ec2:DescribeRegions"
            ],
            "Resource": "*"
        }
    ]
}
