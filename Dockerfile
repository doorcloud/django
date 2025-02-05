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
COPY .env.sample .env
# Expose the port that the Nginx application will use
EXPOSE 8080

# Set the entrypoint
RUN chmod +x entrypoint.sh

# Define the entrypoint to start the Django server
ENTRYPOINT ["/app/entrypoint.sh"]
