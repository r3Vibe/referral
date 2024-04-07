# Base Image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY Pipfile /app/
COPY Pipfile.lock /app/

# Install dependencies
RUN pip install pipenv
RUN pipenv install
RUN pipenv install fastapi uvicorn

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Command to run the FastAPI application
CMD [ "pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
