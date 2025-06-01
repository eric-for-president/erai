ARG PYTHON_VERSION=3.12-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install psycopg2 dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
 && rm -rf /var/lib/apt/lists/*

# Set work directory
RUN mkdir -p /code
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /code

# Collect static files
ENV SECRET_KEY "w=sth#@j4!o-24gd@sxtn^u56&b@u2s+-^_5!+q7eg1x0a9)_g"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "erai_project.wsgi"]
