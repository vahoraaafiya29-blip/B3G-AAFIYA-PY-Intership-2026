while True:
 try:
     num = int(input("Enter a number between 1 and 10:"))

     if 1<=num<=10:
        print("You entered:",num)
        break
     else:
        raise ValueError("Number is not between 1 and 10")
     
 except ValueError as e:
    print("Invalid input:",e)
 except Exception:
    print("Invalid input:please enter only numbers")       
  