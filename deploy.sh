#!/bin/bash

# Останавливаем и удаляем старый контейнер, если он существует
echo "==> Останавливаем старый контейнер..."
docker stop my-backend-app 2>/dev/null || true
docker rm my-backend-app 2>/dev/null || true

# Собираем новый Docker-образ
echo "==> Собираем Docker-образ backend-service:v1..."
docker build -t backend-service:v1 .

# Запускаем свежий контейнер
echo "==> Запускаем новый контейнер..."
docker run -d -p 8000:8000 --name my-backend-app backend-service:v1

echo "==> Готово! Сервис запущен и доступен по адресу: http://localhost:8000/docs"
