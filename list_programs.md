Awesome! Let’s create a mini real-time inspired Python project using lists with different data types + list comprehensions.


---

Project: "Smart Home Dashboard Data"

Goal: Simulate data collected from smart devices in a home (like temperature sensors, light sensors, user status, etc.), all in a mixed-type list. Then use list comprehensions to filter and extract useful insights.


---

Step 1: Mixed-type List Data

smart_home_data = [
    {"device": "thermostat", "temp": 22.5},
    {"device": "camera", "status": "active"},
    {"device": "door_sensor", "status": "closed"},
    {"device": "light", "brightness": 75},
    "Living Room",                      # str
    1623425632,                         # timestamp (int)
    True,                               # someone is home
    ["guest_mode", False],             # nested list
    {"device": "humidity_sensor", "humidity": 55},
    3.14159                             # float (random reading)
]


---

Step 2: Use List Comprehensions to Extract Info

1. Get only all devices with a key 'device':

devices = [item["device"] for item in smart_home_data if isinstance(item, dict) and "device" in item]
print(devices)
# Output: ['thermostat', 'camera', 'door_sensor', 'light', 'humidity_sensor']

2. Extract numeric values (int or float):

numbers = [item for item in smart_home_data if isinstance(item, (int, float))]
print(numbers)
# Output: [1623425632, 3.14159]

3. Extract strings:

strings = [item for item in smart_home_data if isinstance(item, str)]
print(strings)
# Output: ['Living Room']

4. Get all "status" values from device dicts:

statuses = [item["status"] for item in smart_home_data if isinstance(item, dict) and "status" in item]
print(statuses)
# Output: ['active', 'closed']

5. Convert all elements to strings:

all_as_strings = [str(item) for item in smart_home_data]
print(all_as_strings)


---

Bonus: Flatten only nested lists (not dicts)

flat_nested_lists = [element for item in smart_home_data if isinstance(item, list) for element in item]
print(flat_nested_lists)
# Output: ['guest_mode', False]


---

This project touches:

Real-world simulation (IoT-style)

Mixed data types

Dictionaries, strings, booleans, floats, ints, nested lists

List comprehensions with conditions


Want to turn this into a small dashboard or analyzer script with a menu?

_________________________________


Ah gotcha! Let's turn one of those real-life list examples into a complete working Python program with list comprehensions, data extraction, and meaningful output.

We’ll use the E-Commerce Order Example.


---

Project: Order Summary Generator

Goal:

Take mixed-type data from an online order and extract useful info like total price, customer name, items, and delivery status using list comprehensions.


---

Full Python Program:

# Mixed-type list representing an order
order_details = [
    {"product": "Laptop", "price": 999.99, "quantity": 1},
    {"product": "Mouse", "price": 25.5, "quantity": 2},
    "John Doe",                       # Customer name
    1234567890,                       # Order ID
    False,                            # Payment not yet completed
    {"shipping": "Express", "delivered": False},
    ["coupon_applied", True],
    3.99                              # Delivery fee
]

# 1. Extract all product names
product_names = [item["product"] for item in order_details if isinstance(item, dict) and "product" in item]

# 2. Calculate total item cost
total_items_cost = sum(item["price"] * item["quantity"] for item in order_details if isinstance(item, dict) and "price" in item)

# 3. Get customer name (first string)
customer_name = next((item for item in order_details if isinstance(item, str)), "Unknown")

# 4. Get delivery status
delivery_status = next((item["delivered"] for item in order_details if isinstance(item, dict) and "delivered" in item), None)

# 5. Get order ID
order_id = next((item for item in order_details if isinstance(item, int) and item > 1000000000), "N/A")

# 6. Extract flags (like coupon applied)
flags = [element for item in order_details if isinstance(item, list) for element in item]

# 7. Add delivery fee
delivery_fee = next((item for item in order_details if isinstance(item, float)), 0.0)
grand_total = total_items_cost + delivery_fee

# Display summary
print("----- ORDER SUMMARY -----")
print(f"Customer: {customer_name}")
print(f"Order ID: {order_id}")
print(f"Products: {product_names}")
print(f"Item Total: ${total_items_cost:.2f}")
print(f"Delivery Fee: ${delivery_fee:.2f}")
print(f"Grand Total: ${grand_total:.2f}")
print(f"Delivery Status: {'Delivered' if delivery_status else 'Pending'}")
print(f"Flags: {flags}")
print("--------------------------")


---

Sample Output:

----- ORDER SUMMARY -----
Customer: John Doe
Order ID: 1234567890
Products: ['Laptop', 'Mouse']
Item Total: $1050.99
Delivery Fee: $3.99
Grand Total: $1054.98
Delivery Status: Pending
Flags: ['coupon_applied', True]
--------------------------


---

This program uses:

Lists with mixed types

List comprehensions

Conditionals & filtering

next() for smart searching

Real-world use case logic


Want the same kind of full program for one of the other examples like travel, student record, or fitness log?

