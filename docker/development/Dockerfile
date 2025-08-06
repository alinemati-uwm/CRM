# Use an official Python runtime as a parent image
FROM python:3.11.8-slim-bullseye
LABEL maintainer="NAI CRM"


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app


RUN pip install --upgrade pip --no-cache-dir

# Install system dependencies including PDF engines
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libpq-dev \
        postgresql-client \
        gcc \
        python3-dev \
        python3-pip \
        libpango-1.0-0 \
        libpangoft2-1.0-0 \
        libharfbuzz0b \
        libffi-dev \
        libjpeg-dev \
        libopenjp2-7-dev \
        libgdk-pixbuf2.0-0 \
        libcairo2 \
        wkhtmltopdf \
        texlive-latex-base \
        texlive-latex-recommended \
        texlive-fonts-recommended && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*



COPY . /app


# Set the working directory in the container
WORKDIR /app






# Step: Install system dependencies
RUN echo ">>> Updating apt and installing system dependencies..." && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo ">>> System dependencies installed."


# Step: Install Python dependencies with better error handling
# copy the requirements file into tmp
COPY requirements/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm -rf /tmp/*



# Step: Create static directories (collectstatic will be run at container startup)
RUN mkdir -p /app/static \
    && mkdir -p /app/explore_news/static

# Step: Expose port
EXPOSE 8000


# Step: Start the application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "explore_news.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]

