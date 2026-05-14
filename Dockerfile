FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Create user BEFORE using --chown
RUN useradd -ms /bin/sh -u 1001 app

# Install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY --chown=app:app . /app

# Debugging
RUN ls -la /app

# Fix line endings + permissions
RUN sed -i 's/\r$//' /app/script.sh && \
    chmod +x /app/script.sh

USER app

EXPOSE 5000

CMD ["sh", "/app/script.sh"]