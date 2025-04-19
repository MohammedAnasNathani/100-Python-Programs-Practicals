def pizza_order():
    size = input("Choose pizza size (small, medium, large): ").lower()
    toppings = input("Would you like to add toppings (pepperoni, mushrooms, etc.)? (yes/no): ").lower()
    extra_cheese = input("Would you like extra cheese? (yes/no): ").lower()

    prices = {'small': 5, 'medium': 7, 'large': 9}
    toppings_price = 1 if toppings == "yes" else 0
    cheese_price = 2 if extra_cheese == "yes" else 0

    total_price = prices.get(size, 0) + toppings_price + cheese_price
    print(f"Total bill: ${total_price}")

pizza_order()
