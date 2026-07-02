class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Different Currency")
        return self.amount < other.amount

    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Different Currency")
        return self.amount > other.amount


m1 = Money(500, "INR")
m2 = Money(700, "INR")

print(m1 < m2)
print(m1 > m2)