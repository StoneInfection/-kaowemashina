from coffee_base import CoffeeBase, Currency


class CoffeRepository:
    def get_coffe(self, coffe: str):
        amount = CoffeeBase().cost_coffee().get(coffe)
        return amount

    def get_currency(self):
        currency = Currency().currency()
        return currency
