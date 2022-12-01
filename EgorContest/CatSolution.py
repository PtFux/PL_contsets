class AbstractCat:
    def __init__(self):
        self.weight = 0
        self.leftovers = 0

    def eat(self, food: int):
        self.weight += (self.leftovers + food) // 10
        self.leftovers = (self.leftovers + food) % 10

    def __str__(self):
        return f"{type(self).__name__} ({self.weight})"


class Kitten(AbstractCat):
    def __init__(self, weight: int):
        super().__init__()
        self.weight = weight

    def meow(self):
        return "meow..."

    def sleep(self):
        return "Snore" * (self.weight // 5)


class Cat(Kitten):
    def __init__(self, weight: int, nick: str):
        super().__init__(weight)
        self.nick = nick

    def meow(self):
        return "MEOW..."

    def get_name(self):
        return self.nick

    def catch_mice(self):
        return "Got it!"
