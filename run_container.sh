docker build -t receipt-processor .
docker run -d --name receipt-processor -p 8000:8000 receipt-processor