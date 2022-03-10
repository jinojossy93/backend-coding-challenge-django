.PHONY: build start test

build:
	docker-compose build

start:
	docker-compose up

test:
	./manage.py test && flake8
