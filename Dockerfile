# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY app/requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY app/ .

# Expose the port the app runs on
EXPOSE 8080

# Run the application
CMD ["python", "main.py"]