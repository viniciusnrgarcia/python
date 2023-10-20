# Run application
```
cd product

python -m uvicorn main:app --reload --port=8080
```

# Build image
```
docker build -t vnrg/product:0.0.1 .
```

# Running docker 
```
docker run --rm -p 8080:8080 vnrg/product:0.0.1
```

# Running image in swarm mode
```
docker swarm init

docker stack deploy -c docker-compose.yml product

docker stack ps product # stack name

docker stack rm product
```

# Test
```
curl --location 'localhost:8080/v1/product' \
--header 'Bearer Authorization: aslkd-k1dlsfoi382' \
--header 'Content-Type: application/json' \
--data '{
    "id": 232,
    "name": "name1",
    "description": "product1",
    "size":1
}'
```
