def sum_numbers(n):
    if n==1:
        return 1
    else:
        return n+sum_numbers(n-1)
n=21
print("Number=",n)
print("Sum Of Number From 1 to",n,"-",sum_numbers(n))