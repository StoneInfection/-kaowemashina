from repository import CoffeRepository


class CoffeSrvice:

    def get_coffe(self, coffe: str):
        amount = CoffeRepository().get_coffe(coffe)
        return amount

    def get_currency(self):
        currency = CoffeRepository().get_currency()
        return currency

    def balance(self, users_purse: int, balance: int):
            balance += users_purse
            print(balance)
            return balance

    def change(self, amount: int, balance: int):
        change = balance - amount
        return change
