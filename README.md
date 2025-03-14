# Web for AI - Fast API
This repo will be used to share some code samples that are used in the slides and/or exercises centered around backend development in FastAPI.

# Running the examples
Using Docker, it is very easy to run these examples.
If you've installed Docker on your system, open a terminal, go to one of the folders and run ```docker-compose up```.

Wait for the command to finish, and your frontend and backend containers should be up and running.
- Frontend default: ```localhost:4242```
- Backend default: ```localhost:8000``` (e.g. ```localhost:8000/docs``` for Swagger documentation)

You can edit the frontend and backend code, the containers use a mounted volume.
It is possible that you'll need to restart the backend after a change. (```docker restart <container>``` or using Docker Desktop)

# Rickroll
[Over here](https://fastapi.tiangolo.com/)

# Documentation
[https://fastapi.tiangolo.com/](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
