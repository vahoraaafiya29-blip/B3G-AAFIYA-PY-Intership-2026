product={
    "Pen":20,
    "Book":150,
    "Bag":1000,
    "Bottle":500,
    "Pencil":10
}
above_100={product:price for product,price in product.items()if price>100}

print("Products priced above 100:")
print(above_100)