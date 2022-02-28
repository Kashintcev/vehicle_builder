dev-run:
	poetry run python main.py

run-db:
	docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=pass -d postgres

fmt:
	poetry run flake8 vehicle_builder/