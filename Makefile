all: up

up: build_postgres runp build rund 

down: stop

build:
	docker build -t database .

build_postgres:
	docker pull postgres

runi: # doesn't exit correctly when using CTRL+C
	docker run -it --rm -p 8000:8000 --name database-container database

rund:
	# docker run -d -p 8000:8000 --name database-container database
	docker run --name database-container -p 8000:8000 -d --network=mynetwork database

runp:
	docker network create mynetwork
	@sleep 1
	docker run --name pongpostgres -v /tmp/my-pgdata:/var/lib/postgresql/data -e POSTGRES_PASSWORD=backend -p 127.0.0.1:5432:5432 -d --network=mynetwork postgres
	@sleep 1
	# docker run -it --rm postgres psql -h 127.0.0.1 -p 5432 -U postgres -d postgres
	# psql postgresql://postgres:backend@127.0.0.1:5432/po
stop:
	docker stop database-container
	docker stop pongpostgres

exec:
	docker exec -it database-container /bin/bash

execp:
	docker exec -it pongpostgres psql -h localhost -p 5432 -U postgres -d postgres
	# docker exec -it pongpostgres psql postgresql postgresql://postgres:backend@127.0.0.1:5432/postgres

prune:
	docker system prune -af

# deletes container instance, freeing up the resources it was consuming, such as disk space and network ports.
rm: # only needed when using rund, removed automatically in runi (--rm)
	docker rm database-container
	docker rm pongpostgres
	docker network rm mynetwork

# remove Docker image from your local image registry (free disk space) 
remove_image:
	docker rmi database

logs:
	docker logs database-container

logsp:
	docker logs pongpostgres

test:
	google-chrome http://127.0.0.1:8000/blockchainTestApp/blockchainTest/
	
admin:
	google-chrome http://127.0.0.1:8000/admin


.PHONY: all up down build run runi rund stop remove logs exec test admin build_postgres runp execp logsp