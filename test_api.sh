# for each receipt in examples, send a POST request

for filename in examples/*.json; do
    curl -X POST "http://localhost:8000/receipts/process" -H "Content-Type: application/json" -d @$filename

    
done