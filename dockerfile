# Use the official Python image as the base image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install Flask

# Expose the port Flask runs on
EXPOSE 5000


# Command to run on container start
CMD ["python3", "main.py", "--host=0.0.0.0"]
