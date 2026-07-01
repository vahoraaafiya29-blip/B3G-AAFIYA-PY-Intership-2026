def process_order(order):
    try:
        item=order["item"]
        price=order["price"]
    except KeyError:
        print("Error:'item' or'price'key missing in order")
    else:
        print("Order details:")
        print("Item:",item)
        print("Price:",price)
    finally:
        print("Processing complete\n")

order1={"item":"Laptop","Price":50000}
process_order(order1)

order2={"item":"Mobile"}
process_order(order2)

