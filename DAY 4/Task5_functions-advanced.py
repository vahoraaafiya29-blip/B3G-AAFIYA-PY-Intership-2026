from functools import reduce
numbers=[10,45,22,29,89,67]

def find_largest(a,b):
    if a>b:
        return a
    else:
        return b
    
largest=reduce(find_largest,numbers)
print("List Of Number:",numbers)
print("The Largest Number in the List is:",largest)
