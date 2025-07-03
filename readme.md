# Домашня робота. Тема 6. Розширені можливості SQLAlchemy та міграції схеми бази даних

## Технології

- Python 3.10+
- SQLAlchemy
- PostgreSQL (через Docker)
- Alembic
- Faker
- Docker

## Запуск

### 1. Запуск PostgreSQL через Docker
```bash
docker run --name pg-hw6 -p 5432:5432 -e POSTGRES_PASSWORD=mY_VeRy_sEcReT_PaSsWoRd -d postgres
```
### 2. Клонування репозиторію
### 3. Розгортання проєкту за допомогою Poetry
```bash
poetry install
poetry shell
```
### 4. Міграції з Alembic
```bash
poetry run alembic upgrade head
```
### 5. Наповнення тестовими даними
```bash
 poetry run python -m db.seed
```
### 6. Виконання запитів
```bash
 poetry run python main.py
```