def create_counter():
    count=0

    def counter():
        nonlocal count
        count+=1
        return count
    return counter
counter1=create_counter()
counter2=create_counter()

print("Counter 1 Calls:")
print("First Call=",counter1())
print("Second Call=",counter1()) 
print("Third Call=",counter1())
print("Four Call=",counter1())
print("Fifth Call=",counter1())

print("\nCounter 2 Calls:")
print("First Call=",counter2())
print("Second Call=",counter2())
print("Third Call=",counter2())

