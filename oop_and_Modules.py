# 🌟 Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"'{self.amount} {self.currency}'"

    def addition(self, num):
        return self.amount + num

    def total(self, Currency):
        return self.amount + Currency.amount

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1.addition(5))
print(c1.total(c2))
print(c1)

# 🌟 Exercise 2: Import
from func import sum2
print(sum2(2,4))


# 🌟 Exercise 3: String module
import random
import string

random_letters = ''.join(random.choices(string.ascii_letters, k=5))

print(random_letters)


# 🌟 Exercise 4 : Current Date
import datetime
x = datetime.datetime.now()
print(x)