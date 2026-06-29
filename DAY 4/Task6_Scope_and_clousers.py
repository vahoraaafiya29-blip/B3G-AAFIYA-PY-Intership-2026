def make_validator(min_marks):

    def check_marks(marks):
        if marks>=min_marks:
            return"Valid"
        else:
            return"Invalid"
    return check_marks

validator=make_validator(50)

print("Marks=21:",validator(21))
print("Marks=90:",validator(90))
print("Marks=20:",validator(20))
print("Marks=75:",validator(75))