
all: test clean run

APP_NAME?="app"

run: 

	docker-compose up --build -d
	docker logs -f --since=15m -t $(APP_NAME)
	xdg-open 'http://localhost'

###### CLEANING #######

CONTAINERS=$(shell docker ps -a -q)

clean:
	sudo docker ps -a
	-cd tests/test_app && docker-compose down --remove-orphans
	-sudo docker kill 

deepclean: clean
	-rm -rf tables
	-echo "$(CONTAINERS)" && sudo docker rm $(CONTAINERS)
	-sudo docker system prune -a -f --volumes

###### TESTING #######

#OPTIONS
TEST_FUNC?="test_"

test: clean run
	echo "Running tests"
	-docker exec -it $(APP_NAME) python -m pytest -v -s tests/$(TEST_FUNC)*.py