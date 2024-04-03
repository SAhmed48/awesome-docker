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
