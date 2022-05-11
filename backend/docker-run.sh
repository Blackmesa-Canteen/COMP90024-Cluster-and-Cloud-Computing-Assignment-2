# make sure the database is configured properly

docker stop "backend"
docker rm "backend"

docker build -t backend_docker:latest .

docker run -dp 5000:5000 --name backend backend_docker:latest