n=[10,20,30,40,60]
max=float('-inf')
max1=float('-inf')

for n1 in n:
    if n1>max:
        max1=max
        max=n1
    elif n1>max1 and n1!=max:
        max1=n1

print("Second largedst number is:",max1)