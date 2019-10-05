# docker-flask-gunicorn-nginx

Boilerplate project template for a generic dockerized Flask application deployed with gunicorn and Nginx configurations.
## Quickstart
Run in this path:
```sh
$ docker-compose up
```
This will build the docker image and the production-ready Flask app will be running on http://my-public-ip:5001 (or http://localhost:5001 for local machine). 
Static files will be served by Nginx on http://my-public-ip/static/. 

