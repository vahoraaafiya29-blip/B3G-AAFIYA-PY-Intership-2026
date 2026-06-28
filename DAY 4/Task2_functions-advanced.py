def apply_discount(price,percent=10):
    final=price-(price*percent/100)
    print("Final Price:",final)

apply_discount(1000)
apply_discount(1000,percent=20)