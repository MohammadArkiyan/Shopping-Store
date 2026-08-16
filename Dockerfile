FROM python:3.12-slim

# Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System deps needed to build psycopg2 and run health checks (netcat/pg wait)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project source
COPY . .

# Fix the misnamed gitignore file if it exists (has no leading dot in the repo)
RUN mkdir -p /app/staticfiles /app/media

# Generate entrypoint.sh directly inside the image (instead of COPYing it
# from the host) so it can never be broken by the host editor saving it
# with Windows line endings (CRLF) or a UTF-8 BOM — both of which corrupt
# the "#!/bin/sh" shebang and cause "exec: no such file or directory".
RUN printf '%s\n' \
    '#!/bin/sh' \
    'set -e' \
    '' \
    'echo "Waiting for PostgreSQL at ${POSTGRES_HOST:-db}:${POSTGRES_PORT:-5432}..."' \
    'while ! nc -z "${POSTGRES_HOST:-db}" "${POSTGRES_PORT:-5432}"; do' \
    '  sleep 0.5' \
    'done' \
    'echo "PostgreSQL is up."' \
    '' \
    'python manage.py migrate --noinput' \
    'python manage.py collectstatic --noinput' \
    '' \
    'exec gunicorn shoppingstore_project.wsgi:application \' \
    '    --bind 0.0.0.0:8000 \' \
    '    --workers 3' \
    > /app/entrypoint.sh \
    && chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]