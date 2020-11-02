# Assignment Title: Manage multiple Containers in Docker.

#### Help: docs.docker.com or --help

## Motivation:
The purpose of this assignment is how to manage containers in docker.

## Question: Setup 3 different containers:
1) nginx -> deafult port: 80
2) mysql -> deault port: 3306
3) httpd(apache) -> deault port: 8080

All containers will setup using custom name provided by you.
All containers must be run on different ports assigned by you.
Please set environement variable while running MYSQL image as a container.
Hint:
--env or -e MYSQL_RANDOM_ROOT_PASSWORD=yes

To check MYSQL password on startup:
-- docker container logs

Write each setup to run, list, stop and remove containers.

## Solution:

RUN and PULL NGINX:
docker container run --publish 8080:80 --name wbsnginx nginx

Run and PUll Mysql container:

docker container run --env MYSQL_ROOT_PASSWORD=yes --publish 3500:3306 --name dbmysql mysql

RUN AND PULL HTTPD(APACHE):

docker container run --publish 6000:80 --name wbshttp httpd

Stop container:

docker container stop <container-id/container-name>

Remove container:

docker container rm <container-id/container-name>


