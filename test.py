# test.py
import json
import os
import requests
from data_manips import calculate_points

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
        id = response.json()["id"]
        print("id: ", id)

        #Test get
        response = requests.get(f"http://localhost:8000/receipts/{id}/points")
        print(response.json())

