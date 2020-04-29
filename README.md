# myAPI
Required:
1. pull this repo to local
2. pull mysql image: docker pull genschsa/mysql-employees:lastest

How to build & run service:
1. build from Dockerfile: $docker build -t myapi_test:1.2 .
2. run: docker run -p 5000:80 CONTAINER_ID
3. go to browser: localhost:5000
