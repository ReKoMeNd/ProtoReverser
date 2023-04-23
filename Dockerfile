# Use Debian as the base image
FROM debian:latest

# Set the working directory for the application
WORKDIR /app

# Install any necessary dependencies and packages
RUN apt-get update && \
    apt-get -y install cron
