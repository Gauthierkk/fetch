import math
import uuid
import json

def get_receipt_points(id) -> int:
    """
    Retrieves the points for a given receipt ID.

    Args:
        id (str): The receipt ID.

    Returns:
        int: The points for the receipt.
    """
    with open('data.json', 'r') as f:
        data = json.load(f)
        if id in data:
            return data[id]
        else:
            return -1

def add_data(data) -> str:
    """
    Generates a unique identifier for a receipt, calculates points for the receipt,
    and stores the information in a JSON file.

    Args:
        data (dict): A dictionary containing receipt information, including 'retailer',
                     'purchaseDate', 'purchaseTime', 'total', and 'items'.

    Returns:
        str: A unique identifier for the receipt.
    """
    id = str(uuid.uuid4())
    try:
        with open('data.json', 'r') as f:
            data_dict = json.load(f)
    except FileNotFoundError:
        data_dict = {}
    except json.JSONDecodeError:
        data_dict = {}

    data_dict[id] = calculate_points(data)

    with open('data.json', 'w') as f:
        json.dump(data_dict, f)

    return id

def validate_receipt(data) -> bool:
    """
    Validates that the receipt data contains all required fields.

    Args:
        data (dict): A dictionary containing receipt information.

    Returns:
        bool: True if all required fields ('retailer', 'purchaseDate', 
              'purchaseTime', 'total', and 'items') are present, False otherwise.
    """
    return 'retailer' in data and 'purchaseDate' in data and 'purchaseTime' in data and 'total' in data and 'items' in data

def calculate_points(data) -> int:
    """
    Calculates the points for a given receipt.

    Points are calculated as follows:
    - One point for each alphanumeric character in the retailer's name.
    - 50 points if the total is a round dollar.
    - 25 points if the total is a round quarter.
    - 5 points for every 2 items in the receipt.
    - If the trimmed length of an item's description is divisible by 3, add 20% of the item's price.
    - 6 points if the day of purchase is odd.
    - 10 points if the time of purchase is between 14:00 and 16:00.

    Args:
        data (dict): A dictionary containing receipt information.

    Returns:
        int: The points for the receipt.
    """
    points = 0

    # One point for each alphanumeric character
    for char in data['retailer']:
        if char.isalnum():
            points += 1
    
    # 50 points if total is a round dollar
    if data['total'].endswith('.00'):
        points += 75
    
    # 25 points if total is a round quarter
    if data['total'].endswith(('.25', '.50', '.75')):
        points += 25
    
    # 5 points for every 2 items in the receipt
    points += len(data['items']) // 2 * 5

    # If trim length is divisible by 3, add 20% of the item price
    for item in data['items']:
        if len(item['shortDescription'].strip()) % 3 == 0:
            points += math.ceil(float(item['price']) * 0.2)

    # 6 points if the day of purchase is odd
    if int(data['purchaseDate'][-2:]) % 2 == 1:
        points += 6

    # 10 points if the time of purchase is between 14:00 and 16:00    
    if '14:' <= data['purchaseTime'] < '16:':
        points += 10

    return points
