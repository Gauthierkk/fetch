# test.py
import json
import uuid
import os
import requests
from data_manips import validate_receipt

#Testing validate receipts

# Testing point calculations
test_file_directory = "examples"
filename = [f"{test_file_directory}/{file}" for file in os.listdir(test_file_directory)]

headers = {
            "Content-Type": "application/json"
}

for filename in filename:
    with open(filename, "r") as f:
        print("Testing: ", filename.split("/")[-1])
        payload = json.load(f)

        #Test post
        response = requests.post("http://localhost:8000/receipts/process", headers=headers, json=payload)
        if response.status_code != 200:
            print("Invalid receipt")
            continue
        id = response.json()["id"]

        #Test get
        response = requests.get(f"http://localhost:8000/receipts/{id}/points")
        if response.status_code != 200:
            print("receipt does not exist")
        else: print(response.json())

