# Official python base image from docker hub
FROM python:3.10-slim

# Set the working dir
WORKDIR /app

# Copy dedependicies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8080


# Application startup command
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
