# Pull base image
FROM python:3.6-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install pipenv
COPY ./Pipfile /code/Pipfile
RUN pipenv install --system --skip-lock

# Run the image as a non-root user (in production)
RUN adduser --disabled-login myuser
USER myuser

#add code from working directory
COPY . /code/

#CMD required by heroku
CMD gunicorn --bind 0.0.0.0:$PORT tensorai.wsgi
