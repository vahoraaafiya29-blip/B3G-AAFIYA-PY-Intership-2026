class InvalidAgeError(Exception):
    pass

def register_user(age):

    if age<0 or age>120:
        raise InvalidAgeError("Invalid age entered.")
    print("User registered successfully.")

try:
        register_user(25)
        register_user(150)

except InvalidAgeError as e:
     print(e)        
