from repository import CoffeRepository


class CoffeSrvice:
    def __init__(self):
        self.repo = CoffeRepository()

    def get_coffe(self, coffe: str):
        amount = self.repo.get_coffe(coffe)
        return amount

    def get_currency(self):
        currency = self.repo.get_currency()
        return currency

    def calculating_balance(self, users_purse: int, balance: int):
            balance += users_purse
            return balance

    def calculating_change(self, amount: int, balance: int):
        change = balance - amount
        return change
