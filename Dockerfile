# Use an official Helm base image (adjust the version as needed)
FROM alpine/helm:3.7.0

# Set the working directory in the container
WORKDIR /app

# Copy the Helm chart files from the current directory into the container
COPY ./ /app

EXPOSE 3001
# Optionally, you can set environment variables or add other configurations here

# Define the command to run (e.g., Helm commands)
# CMD ["helm", "install", "my-release", "."]
