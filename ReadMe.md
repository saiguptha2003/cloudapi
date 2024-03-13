## Cloud Computing Presentation QUICK Tutorial 
### Flask Server Hosting in AWS EC2
### github link : <a href='https://github.com/saiguptha2003/cloudapi.git'>https://github.com/saiguptha2003/cloudapi.git</a>

#### dockerfile Content:
```dockerfile


```

#### After creating the Dockerfile, build your Docker image by navigating to the directory containing the Dockerfile and running:

```bash

docker build -t flask-app .

```
#### Once the image is built, you can run the container using:


```bash

docker run -p 8080:5000 flask-app

```
