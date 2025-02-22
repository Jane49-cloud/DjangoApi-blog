# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

# Copy the project files
COPY . /app/

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# docker-compose run web python manage.py migrate ---starts docker 
# docker-compose run web python manage.py migrate ---run the project withon docker


