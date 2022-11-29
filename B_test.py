from CatSolution import *

abscat = AbstractCat()
abscat.eat(125)
abscat.eat(17)
print(abscat)

kit = Kitten(21)
print(kit.sleep())

cat = Cat(83, "Molly")
print(cat.meow())
print(cat.get_name())
