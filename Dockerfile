ARG PYTHON_VERSION=3.12-slim
FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system deps (psycopg2, Pillow, etc.)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
 && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /code

# Install Python deps (cached if requirements.txt unchanged)
COPY requirements.txt .


# Copy project files (after deps so cache works better)
COPY . .

# Expose port
EXPOSE 8000

# Run Gunicorn (production-ready server)
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "erai_project.wsgi:application"]
