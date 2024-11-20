# Use the official Python image from Docker Hub as the base image
FROM python:latest

# Copy the current directory's contents into the container at /app
COPY . /app

# Set the working directory inside the container to /app
WORKDIR /app

# Run the Python script when the container starts
RUN pip install --no-cache-dir -r requirements.txt

# Will use port 8000 to expose this service
EXPOSE 8000

# Run webservice
CMD ["python", "controller.py"]