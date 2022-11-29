class PearBasket:
    def __init__(self, amount: int):
        if amount > 0:
            self.amount = amount
        else:
            self.amount = 0

    def __add__(self, other):
        if type(other) is PearBasket:
            return PearBasket(self.amount + other.amount)

    def __sub__(self, other: int):
        if type(other) is int:
            self.amount = max(0, self.amount - other)
            return self

    def __floordiv__(self, other: int):
        if type(other) is int:
            baskets = [PearBasket(self.amount//other) for i in range(other)]
            if self.amount % other:
                baskets.append(PearBasket(self.amount % other))
            return baskets

    def __mod__(self, other: int):
        return self.amount % other

    def __repr__(self):
        return f"PearsBasket({self.amount})"

    def __str__(self):
        return str(self.amount)
