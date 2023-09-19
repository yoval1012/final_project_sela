FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose port 3001 for your Flask app
EXPOSE 3001

# Define the command to run your Flask app
CMD ["python", "app.py"]
