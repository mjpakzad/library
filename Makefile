up:
	docker compose up -d

build:
	docker compose up -d --build

setup:
	docker compose up -d \
	&& docker exec -it web "cd goodreads && python3 manage.py migrate" \
	&& docker exec -it web "cd goodreads && python3 manage.py loaddata user_data.json books_data.json" \
	&& docker exec -it web "cd goodreads && python3 manage.py createsuperuser"

down:
	docker compose down
