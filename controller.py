import json
import os
from flask import Flask, jsonify, request, session
from data_manips import add_data, validate_receipt, get_receipt_points

app = Flask(__name__)
data = {}

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    """
    Processes a receipt and stores the receipt information in a JSON file.

    The receipt information should contain the following fields:
    retailer, purchaseDate, purchaseTime, total, and items (list).
   
    Returns a JSON response with the receipt ID if the receipt is valid, or
    a JSON response with an error message if the receipt is invalid.
    """

    data = request.get_json()
    if not validate_receipt(data):
        return jsonify({"error": "Invalid receipt"}), 400
    
    else :  
        id = add_data(data)
        return jsonify({"id":id}), 200
    

@app.route('/receipts/<id>/points', methods=['GET'])
def get_points(id):
    """
    Retrieves the points for a receipt.

    Args:
        id (str): The receipt ID.

    Returns:
        JSON containing the points for the receipt, or an error message
        if the receipt does not exist or the data file does not exist.
    """
    
    if not os.path.exists('data.json'):
        return jsonify({"error": "No data!"}), 400
    else:
        pts = get_receipt_points(id)
        if pts == -1:
            return jsonify({"error": "Receipt does not exist!"}), 400
        else:
            return jsonify({"points": pts}), 200
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)