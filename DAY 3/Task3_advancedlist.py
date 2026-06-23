Number=[45,23,90,12,34,56,11,90,78,34,78,23,67,23,21]
unique_Number=[]

for num in Number:
     if num not in unique_Number:
           unique_Number.append(num)

print("Original List:")
print(Number)
print("\nList after removing duplicate:")
print(unique_Number)           