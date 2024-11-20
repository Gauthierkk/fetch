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
3. Run the following command to build the Docker image and run the container:

`./run_docker.sh`

Let's break down what this script does:

1.  `docker stop receipt-processor` - stops the running container
    `docker rm receipt-processor` - removes the stopped container
    This ensures you can run the image from fresh. However be aware if you have a container with this name and/or image name running already they WILL be stopped.
2.

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

There is an attached `test.py` script to run several receipts at once against the API. You may use or edit it as you please. In order to use it, make sure your receipts are all stored in the `examples` directory. First, make sure the service is up and running locally on port 8000 (You should have it already running on this port if you've followed the instructions. Then run `python3 test.py`
