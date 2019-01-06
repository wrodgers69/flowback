# Pull base image
FROM python:3.6-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /flowback

# Install dependencies
RUN pip install pipenv
COPY ./Pipfile /flowback/Pipfile
RUN pipenv install --system --skip-lock

# Copy project
COPY . /flowback/

# Run the image as a non-root user (in production)
#RUN adduser --disabled-login myuser
#USER myuser

#CMD required by heroku
CMD gunicorn --bind 0.0.0.0:$PORT tensorai.wsgi
