def apply_discount(price,percent=10):
    discount=price*percent/100
    final_price=price-discount
    return final_price

print("price After Default Discount:",apply_discount(4500))
print("price After 20% Discount:",apply_discount(6500,percent=20))
