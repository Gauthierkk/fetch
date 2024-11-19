import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    data = request.get_json()
    return jsonify(data)


# 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)