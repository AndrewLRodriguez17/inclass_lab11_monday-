# customers.py
# Author: Andrew Rodriguez
# Module 11 Lab: Customer Dictionary & Lookup


print("--- Exercise 1 ---")
customer = {
    "name": "Alice", # Key : Value
    "Name": "Not Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400
}

print(customer["name"])  # Output: Alice
print(customer["email"])  # Output: alice@example.com
print(customer["tier"])  # Output: gold
print(customer["ytd_spend"])  # Output: 12400


print("--- Exercise 2 ---")
customer["phone"] = "555-5555"  # Adding a new key-value pair
print(customer)
customer["tier"] = "platinum"  # Updating an existing value
print(customer)
del customer['Name']
print(customer)

print(customer.get('ytd_spend', 0))


print("--- Exercise 3 ---")
print(customer.get("email", "no email on file"))

#try:
#    print(customer["email"])
#except KeyError as error:
#   print("KeyError caught:", {error}")

print("--- Exercise 4 ---")
for key in customer:
    print(key, ":", customer[key])

print("--- Exercise 5 ---")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.1,
    "platinum": 0.15
}

tier = "gold"

discount = tier_discounts.get(tier, 0)

purchase_price = 200
final_price = purchase_price * (1 - discount)

print("Tier:", tier)
print("Discount:", discount * 100, "%")
print("Final Price:", final_price)


print("--- Exercise 6 ---")

dict1 = {
    "name": "Alice",
    "tier": "silver"
}

dict2 = {
    "name": "Bob",
    "tier": "gold"
}

dict3 = {
    "name": "Charlie",
    "tier": "platinum"
}  

customers = [dict1, dict2, dict3]

purchase_price = 300

for customer in customers:
    tier = customer.get("tier", "bronze")
    discount = tier_discounts.get(tier, 0)
    final_price = purchase_price * (1 - discount)
    
    print("Customer:", customer["name"])
    print("Tier:", tier)
    print("Discount:", discount * 100, "%")
    print("Final Price:", final_price)
    print()

print("--- Exercise 7 ---")

catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Widget C": {
        "price": 49.99,
        "stock": 8
    }
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(product, "LOW STOCK")


print("--- Exercise 8 ---")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    
    summary[region] = summary.get(region, 0) + amount

for region in sorted(summary):
    print(region, ":", summary[region])


# Reflection Questions:
# 1. You would use the .get() when you are wanting to look something up in
# a database or dictionary but you don't want to get an error but the brackets,
# you would use them for just print something out
# 2. This reminds me of when you want to get a big look at a number database and
# create a spreadsheet of the data you collected but python may be a better way since
# you don't have to actually write it all down and just make a coding to use the data you got