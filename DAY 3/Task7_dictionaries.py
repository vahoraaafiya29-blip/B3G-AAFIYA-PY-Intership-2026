
# Inventory System

inventory = {
    "Pen": 20,
    "Notebook": 15,
    "Pencil": 30
}

while True:
    print("\n--- INVENTORY SYSTEM ---")
    print("1. Add new stock")
    print("2. Sell product")
    print("3. Show inventory")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity to add: "))

        if product in inventory:
            inventory[product] += quantity
        else:
            inventory[product] = quantity

        print("Stock added successfully.")

    elif choice == "2":
        product = input("Enter product name to sell: ")
        quantity = int(input("Enter quantity to sell: "))

        if product in inventory:
            if inventory[product] >= quantity:
                inventory[product] -= quantity
                print("Product sold successfully.")
            else:
                print("Not enough stock available.")
        else:
            print("Product does not exist in inventory.")

    elif choice == "3":
        print("\nCurrent Inventory:")
        for product, quantity in inventory.items():
            print(product, ":", quantity)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")