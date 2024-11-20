#Remove previous container
docker stop receipt-processor
docker rm receipt-processor

# Build docker container
docker build -t receipt-processor .

# Run docker
docker run -d --name receipt-processor -p 8000:8000 receipt-processor