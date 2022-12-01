# Simple App

---

## Stack Documentation

### Docker

- [Docker](https://docs.docker.com/)
- [Docker Compose](https://github.com/compose-spec/compose-spec/blob/master/spec.md)

### Server

- [gunicorn](https://docs.gunicorn.org/en/stable/configure.html)

### Backend Stack

- [Python](https://docs.python.org/3.9/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)

### FrontEnd Stack

- [PyScript](https://pyscript.net/)

## Developer Notes

### Start/Status/Stop Commands

- build and start the container
  - `docker-compose up --build -d`
- container status
  - `docker-compose ps -a`
- run a command in the container
  - `docker-compose exec -option simple_app <command>`
- stop and remove running containers
  - `docker-compose down --remove-orphans`
- stop all running containers
  - `sudo docker kill $(sudo docker ps -q)`
- remove all stopped containers
  - `sudo docker rm $(sudo docker ps -a -q)`

### Read Logs

```sh
docker logs --since=15m -t simple_app
```

*follows as a background process*

```sh
docker logs -f --since=15m -t <container> &`
```

---

### Misc Notes
