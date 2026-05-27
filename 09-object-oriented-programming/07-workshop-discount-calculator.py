# Workshop: Build a Discount Calculator
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price):
        pass

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price * (1 - self.percent / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, price):
        return max(0, price - self.amount)

class DiscountEngine:
    def __init__(self, strategies):
        self.strategies = strategies

    def calculate(self, price):
        final = price
        for s in self.strategies:
            final = s.apply(final)
        return final
