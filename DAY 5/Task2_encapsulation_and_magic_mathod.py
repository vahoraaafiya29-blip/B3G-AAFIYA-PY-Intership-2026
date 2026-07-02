class Fraction:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

result = f1 + f2

print(result)