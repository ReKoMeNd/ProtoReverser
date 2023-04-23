# Use Debian as the base image
FROM debian:latest

# Set the working directory for the application
WORKDIR /app

# Install any necessary dependencies and packages
RUN apt-get update && \
    apt-get -y install cron

RUN crontab -l | { cat; echo "*/15 * * * * bash /root/botnetIPlistCron.sh"; } | crontab -

# Run the command on container startup
CMD cron

RUN cat ipblocklist.json
