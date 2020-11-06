## Assignment 2 

#### Create a custom image of nodejs application.

#### Instructions:

Build your own image using docker file.
Create node.js app on your local, dockerize it.

1. **Build Dockerfile**
2. **Test it**
3. **Push it**
4. **Run it**

###### Note:
Use alpine version of official node.
See result on localhost.
Tag image and push docker hub.
Remove from local and pull it from docker and then run.


## Solution

Create a directory **node-app** and change directory node-app.

Create a Dockerfile in it.

```
# Specifies the base image we're extending
FROM node:12.19.0

# create a new working directory
RUN mkdir -p /user/app

# Specify the "working directory" for the rest of the Dockerfile
WORKDIR /src/app

COPY ./package.json ./package-lock.json /user/app/

# Add application code
COPY . /src/app

RUN npm install

EXPOSE 9000

CMD ["npm", "run", "start:server"]
```

###### Build Image using above Dockerfile

```
docker image build -t initial-nodeapp . # dot(.) represents current directory which contain DockerFile
```

**Run image as a process into container**

```
docker container run -p 3000:9000 initial-nodeapp
```

#### Push image to docker hub.

```
docker image push salmanAhmed/initial-nodeapp

docker login 
```