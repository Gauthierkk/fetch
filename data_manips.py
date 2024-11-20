import math

def validate_receipt(data) -> bool:
    return 'retailer' in data and 'purchaseDate' in data and 'purchaseTime' in data and 'total' in data and 'items' in data

def calculate_points(data) -> int:
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
