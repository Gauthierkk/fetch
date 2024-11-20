import json
import uuid
from flask import Flask, jsonify, request
from data_manips import calculate_points, validate_receipt

app = Flask(__name__)

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    data = request.get_json()

    #make sure all fields are present
    if not validate_receipt(data):
        return jsonify({"error": "Invalid receipt"}), 400
    
    # calculate points, generate uuid and save to temporary file
    else :  
        id = uuid.uuid4()
        points = calculate_points(data)
        with open('data.json', 'a') as f:
            json.dump({str(id): points}, f)
            f.write('\n')

        return jsonify({"id":id}), 200
    

@app.route('/receipts/<id>/points', methods=['GET'])
def get_points(id):

    # Check if data.json exists
    if not os.path.exists('data.json'):
        return jsonify({"error": "No data!"}), 400
    
    # Find points for this id
    with open('data.json', 'r') as f:
        data = json.load(f)
        if id not in data:
            return jsonify({"error": "Receipt not found"}), 400
        else:
            return jsonify({"points": data[id]}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)