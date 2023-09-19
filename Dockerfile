FROM python:3.8-alpine

# Create a non-root user
RUN useradd -m yuval

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Change ownership of the application directory to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER yuval

# Expose port 3001 for your Flask app
EXPOSE 3001

# Define the command to run your Flask app
CMD ["python", "app.py"]
