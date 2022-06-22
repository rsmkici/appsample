Hello All,

This basic code sample is being written to aim finding the severity of the vulnerabilities which is stored as nucleic-template.

To dockerize the application please follow the steps:

docker image build -t appsample https://github.com/rsmkici/appsample.git

docker run -it  appsample:latest mainlinux.py springboot-log4j-rce.yaml


