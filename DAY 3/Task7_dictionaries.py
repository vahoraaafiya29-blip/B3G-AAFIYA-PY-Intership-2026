inventory = {
    "Pen": 100,
    "Notebook": 50
}

inventory["Pen"]=inventory["Pen"] + 10
product="Notebook"

if"Notebook"in inventory:
    inventory["Notebook"]=inventory["Notebook"]-1
    print("Notebook sold")
else:
    print("Notebook Not Found")
    product="Bag"

    if "Bag" in inventory:
        inventory["Bag"]=inventory["Bag"]-1
    else:
        print("Bag Not Found")
        print("Updated Inventory:")
        print(inventory)
