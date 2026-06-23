price=[100,200,300,400,500,600,700,800,900,1000]
avg_price=sum(price)/len(price)
above_price=[p1 for p1 in price if p1>avg_price]


print("List of Prices:",price)
print("Average price is:",avg_price)
print("Above prices are:",above_price) 



