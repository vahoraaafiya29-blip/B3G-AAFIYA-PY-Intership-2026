def build_invoice(customer, *prices,**details):
    print("Customer Name:",customer)
    print("Total Price:",sum(prices))
    
    for key,value in details.items():
     print(key,":",value)

build_invoice("Aafiya",500,300,200,discount=50,tax=18)     