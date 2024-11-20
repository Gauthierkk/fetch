# Receipt Processor API

=========================

## Overview

The Receipt Processor API is a Flask-based API that processes receipts and calculates points based on the receipt data. This API is designed to be run in a Docker container.

## Prerequisites

- Docker installed on your system
- Python 3.x (for running the API outside of Docker)
- The different libraries outlined in the requirements.txt file

## Running the API in Docker

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the following command to build the Docker image:

```bash
docker build -t receipt-processor .
```

4. Run the following command to start the Docker container:

```bash
docker run -d --name receipt-processor -p 8000:8000 receipt-processor
```

This will start the API in detached mode, mapping port 8000 on the host machine to port 8000 in the container.

## Using the API

### Processing Receipts

To process a receipt, send a POST request to `http://localhost:8000/receipts/process` with the receipt data in JSON format. The receipt data should contain the following fields:

- `retailer`: The name of the retailer
- `purchaseDate`: The date of purchase in YYYY-MM-DD format
- `purchaseTime`: The time of purchase in HH:MM format
- `items`: A list of items purchased, each containing `shortDescription` and `price` fields
- `total`: The total cost of the purchase

Example request:

```bash
curl -X POST "http://localhost:8000/receipts/process" -H "Content-Type: application/json" -d '{"retailer": "Target", "purchaseDate": "2022-01-01", "purchaseTime": "13:01", "items": [{"shortDescription": "Mountain Dew 12PK", "price": "6.49"}], "total": "6.49"}'
```

The API will return a JSON response containing the receipt ID.

### Retrieving Points

To retrieve the points for a receipt, send a GET request to `http://localhost:8000/receipts/<id>/points`, replacing `<id>` with the receipt ID returned in the previous step.

Example request:

```bash
curl -X GET "http://localhost:8000/receipts/12345/points"
```

The API will return a JSON response containing the points for the receipt.

## Testing the API

You can test the API using the `test_api.sh` script provided in the repository. This script sends a series of POST requests to the API with sample receipt data and retrieves the points for each receipt.

To run the tests, navigate to the project directory and run the following command:

```bash
./test_api.sh
```

This will run the tests and display the results.
