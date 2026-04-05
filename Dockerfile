# NSFW Killer Bot - Docker Ready (2026 optimized)
FROM python:3.11-slim

# System dependencies for OpenCV, ONNX, Torch CPU
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only requirements first (cache optimization)
COPY requirements.txt .

# Install all your exact libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Make scripts executable
RUN chmod +x start setup

# Expose port (Railway/Render ke liye)
EXPOSE 8080

# Environment variables will come from .env or platform
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["bash", "start"]
