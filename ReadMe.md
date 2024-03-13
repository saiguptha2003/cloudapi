## Cloud Computing Presentation QUICK Tutorial 
### Flask Server Hosting in AWS EC2
### github  : <a href='https://github.com/saiguptha2003/cloudapi.git'>https://github.com/saiguptha2003/cloudapi.git</a>

#### dockerfile Content:
```dockerfile
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

```

#### After creating the Dockerfile, build your Docker image by navigating to the directory containing the Dockerfile and running:

```bash

docker build -t flask-app .

```
#### Once the image is built, you can run the container using:


```bash

docker run -p 8080:5000 flask-app

```
## Output:

```json

{
  "message": "welcome to flaskServer",
  "site_name": "flaskserver",
  "team_members": [
    {
      "grade": "A",
      "group": "Group-3",
      "id": 10,
      "name": "KANDULA AYYAPPA",
      "roll_number": "AP21110010053"
    },
    {
      "grade": "A",
      "id": 11,
      "name": "JENIL PADSHALA",
      "roll_number": "AP21110010064"
    },
    {
      "grade": "B",
      "id": 12,
      "name": "CHAGANTIPATI AETESH",
      "roll_number": "AP21110010079"
    },
    {
      "grade": "B",
      "id": 13,
      "name": "BOLLINENI ROHITH",
      "roll_number": "AP21110010081"
    },
    {
      "grade": "B",
      "id": 14,
      "name": "V D PANDURANGA SAI GUPTHA",
      "roll_number": "AP21110010091"
    }
  ],
  "topic_name": "amazon ec2"
}

```
