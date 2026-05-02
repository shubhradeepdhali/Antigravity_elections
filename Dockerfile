# Use an official lightweight Python image.
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all local files into the container
COPY . .

# Run the web service on container startup using gunicorn
# Cloud Run injects the PORT environment variable automatically (defaults to 8080)
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 backend:app
