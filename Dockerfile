# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the content (Python script or other files)
COPY . .

# Install any dependencies if needed (e.g., pip install)
# RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the application
CMD ["python", "app.py"]
