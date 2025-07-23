products = {"Apple": 50, "Banana": 20, "Milk": 30}
cart = {}

while True:
    print("\nAvailable products:")
    for item, price in products.items():
        print(f"{item} - ₹{price}")
    choice = input("Enter product name to add to cart (or 'checkout' to finish): ")
    if choice.lower() == 'checkout':
        break
    if choice in products:
        qty = int(input("Enter quantity: "))
        cart[choice] = cart.get(choice, 0) + qty
    else:
        print("Product not available!")

# Calculate total
total = 0
print("\nYour Cart:")
for item, qty in cart.items():
    price = products[item] * qty
    print(f"{item} x {qty} = ₹{price}")
    total += price

print(f"Total amount: ₹{total}")
