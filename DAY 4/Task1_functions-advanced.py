def build_invoice(customer_name, *args,**kwargs):
    total=sum(args)

    print("Customer Name:",customer_name)
    print("Total Price:",total)
    print("Extra Details:")
    for key,value in kwargs.items():
     print(key,":",value)

build_invoice("Aafiya",500,300,200,discount=50,tax=18)     