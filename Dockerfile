# Base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a non-root user
RUN groupadd -r celery && useradd -r -g celery celery

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project and the start script
COPY . /app/
COPY start_beat_flower.sh /app/start_beat_flower.sh

# Change ownership of the application files
RUN chown -R celery:celery /app

# Switch to the non-root user
USER celery

# Command to run
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
