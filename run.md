# Инструкция по запуску проекта

1. Клонируйте репозиторий(либо скачайте просто zipкой):
```bash
git clone <https://github.com/H1k1r1/marketplace-architecture>
cd marketplace-architecture
```
2. Запустите сервисы:
```bash
docker-compose up -d
```

3. Проверки:
```bash
docker-compose ps #контейнеры

curl http://localhost:5000/health #product

curl http://localhost:5001/health #user

#endpoints
#product:
curl http://localhost:5000/api/products
curl http://localhost:5000/api/products/1
#user:
curl http://localhost:5001/api/users
curl http://localhost:5001/api/users/1
```
4. Остановка:
```bash
docker-compose down
```
# Логи:
```bash
# Все логи
docker-compose logs

# Логи конкретного сервиса
docker-compose logs product-service
docker-compose logs user-service
```
# Пересборка:
```bash
docker-compose build
docker-compose up -d
```
# Tестирование health-check:
```bash
#!/bin/bash
echo "Testing Product Service..."
curl -s http://localhost:5000/health | python3 -m json.tool

echo -e "\nTesting User Service..."
curl -s http://localhost:5001/health | python3 -m json.tool
```
# Если не работает:
1. Ребут сервисов:
```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```
2. Порты:
```bash
lsof -i :5000
lsof -i :5001
```
3. Сеть:
```bash
docker network inspect marketplace-architecture_marketplace-network
```
