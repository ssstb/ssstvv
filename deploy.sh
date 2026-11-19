#!/bin/bash
set -e

echo "==> Останавливаем старые контейнеры..."
docker compose down

echo "==> Собираем и запускаем сервисы..."
docker compose up --build -d

echo "==> Готово! Сервис запущен и доступен по адресу: http://localhost:8000/docs"
