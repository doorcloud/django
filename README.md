# Launching a Django (Python) Application with Docker

This guide explains how to set up and launch a Django (Python) application using Docker.

## Prerequisites

Before starting, ensure you have the following tools installed on your machine:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Django](https://www.djangoproject.com/)

## Dockerfile Content

This repository contains a Docker setup for a Django application with Nginx as a reverse proxy.

```Dockerfile
# Use a Python image as a base
FROM python:3.10

RUN apt-get update \
    && apt-get install -y \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the working directory
COPY requirements.txt .

# Copy the Nginx configuration file into the container
COPY nginx.conf /etc/nginx/sites-available/default

# Configure Nginx to redirect logs to the console
RUN sed -i 's/access_log \/var\/log\/nginx\/access.log;/access_log \/dev\/stdout;/g' /etc/nginx/nginx.conf \
    && sed -i 's/error_log \/var\/log\/nginx\/error.log;/error_log \/dev\/stderr;/g' /etc/nginx/nginx.conf

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application into the working directory
COPY . .

# Expose the port that the Nginx application will use
EXPOSE 80

# Set the entrypoint
RUN chmod +x entrypoint.sh

# Define the entrypoint to start the Django server
ENTRYPOINT ["/app/entrypoint.sh"]

```
## Steps to Launch the Application

1. Build the Docker Image

To build the Docker image, use the following command in the directory containing the Dockerfile:

```
docker build -t door-django .
```

2. Run the Container

Once the image is built, run a container from this image:

```
docker run -p 8080:80 door-django
```

3. Access the Application

Open your browser and go to the following URL to see your application running:

```
http://localhost:8080
```

4. Environment Variables

If you need to configure additional environment variables, modify the .env file that was copied into the container during the image build.

## Publishing the Image on Docker Hub

1. Log In to Docker Hub

Before publishing your image, log in to Docker Hub with your Docker account:

```
docker login
```

2. Tag the Image

Tag the image you built with your Docker Hub username and the image name:

```
docker tag door-django your_dockerhub_username/door-django:latest
```
Replace your_dockerhub_username with your Docker Hub username.

3. Push the Image to Docker Hub

Push the tagged image to Docker Hub:

```
docker push your_dockerhub_username/door-django:latest
```

