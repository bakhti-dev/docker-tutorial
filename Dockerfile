FROM python:3.11

# Prevent Python from writing .pyc files and enable unbuffered stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Collect static files for production (if applicable)
RUN python manage.py collectstatic --noinput

# Expose application port
EXPOSE 8000

# Default command will be overridden by Docker Compose services
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]











# FROM python:3.11

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# COPY . .

# RUN python manage.py collectstatic --noinput

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]