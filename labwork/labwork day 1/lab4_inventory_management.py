# Python Lab: 6th July 2026
# Lab 4: Inventory Management

inventory = {
    "Laptop": 15,
    "Mouse": 40,
    "Keyboard": 25,
    "Monitor": 10
}

print("Current inventory:")
for product, stock in inventory.items():
    print(product, ":", stock)

new_product = input("\nEnter new product name to add: ")
new_stock = int(input("Enter stock quantity: "))
inventory[new_product] = new_stock

update_product = input("\nEnter product name to update stock: ")
if update_product in inventory:
    updated_stock = int(input("Enter new stock quantity: "))
    inventory[update_product] = updated_stock
else:
    print("Product not found.")

remove_product = input("\nEnter product name to remove: ")
if remove_product in inventory:
    del inventory[remove_product]
else:
    print("Product not found.")

print("\nProducts with stock less than 20:")
low_stock_found = False
for product, stock in inventory.items():
    if stock < 20:
        print(product, ":", stock)
        low_stock_found = True

if not low_stock_found:
    print("No products with stock less than 20.")

total_items = sum(inventory.values())
print("\nTotal number of items in inventory:", total_items)

print("\nFinal inventory:")
for product, stock in inventory.items():
    print(product, ":", stock)
