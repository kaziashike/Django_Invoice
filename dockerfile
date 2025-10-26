# Use a lightweight Python image
FROM python:3.11-slim

# Prevent Python from writing .pyc files & buffering stdout
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy dependency list first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Set working directory to where manage.py is located
WORKDIR /app/invoice_system

# Create directory for static files
RUN mkdir -p staticfiles

# Expose port (Render sets $PORT automatically)
EXPOSE $PORT

# Run migrations and start the Django server
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn invoice_system.wsgi:application --bind 0.0.0.0:$PORT"]