.PHONY: up down logs migrate seed test fmt lint

up:
	docker compose up -d --build

down:
	docker compose down -v

logs:
	docker compose logs -f --tail=100

migrate:
	docker compose exec backend alembic upgrade head

seed:
	docker compose exec backend python -m pms.scripts.seed

test:
	docker compose exec backend pytest -q

fmt:
	docker compose exec backend ruff format . && ruff check --fix .

lint:
	docker compose exec frontend npm run lint
