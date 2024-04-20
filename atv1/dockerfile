# Use the official Python image from the Docker Hub
FROM python:3.9

# Install Redis server
RUN apt-get update && \
    apt-get install -y redis-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Install the required Python packages
RUN pip install --no-cache-dir redis

# Copy the Python script into the container
COPY app.py .

# Expose the Redis port
EXPOSE 6379

# Run Python script to check if Redis is empty and add a key if needed
CMD ["sh", "-c", "if ! service redis-server status; then service redis-server start; fi && python app.py"]
