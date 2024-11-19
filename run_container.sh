docker build -t receipt-processor .
docker run -d --name freceipt-processor -p 8000:8000 fastapi-app
