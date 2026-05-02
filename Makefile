-include .env
export

.PHONY: up down reset db

up:
	docker compose up --build -d

down:
	docker compose down

reset:
	docker compose down --volumes --remove-orphans
	docker compose up --build -d

db:
	docker compose up -d db
	docker exec -it my-mysql-db mysql -u user -p
