from functools import reduce

numbers=[10,45,22,89,67]

largest=reduce(lambda a,b:a if a>b else b,numbers)

print("Largest Number:",largest)