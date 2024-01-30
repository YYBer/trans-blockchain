all: compose

compose:
	docker-compose up --build -d

decompose:
	docker-compose down

exec_transcendence:
	docker-compose exec transcendence /bin/bash
	
logs_transcendence:
	docker-compose logs transcendence

logs_postgres:
	docker-compose logs postgres

prune:
	docker system prune -af

remove_image:
	docker rmi -f transcendence
	docker rmi -f postgres

html_test:
	google-chrome http://127.0.0.1:8000
	
db_admin:
	google-chrome http://127.0.0.1:8000/admin

game: 
	python3 trans_autotest_game.py

tour:
	python3 trans_autotest_tournament.py

setr: decompose
	make compose
	sleep 5
	make game
	sleep 5
	make db_admin
	sleep 2
	clear
	make logs_transcendence

set:compose
	sleep 5
	make game
	sleep 5
	make db_admin
	sleep 2
	clear
	make logs_transcendence
