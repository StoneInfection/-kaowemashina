from coffee_base import MoneyCoffeeMachineBase


class MoneyCoffeeMachine:
    def subtract_money(self, change: int):
        money = MoneyCoffeeMachineBase().money_coffee_machine()
        while change != 0:
            for key in money:
                if change >= key:
                    change = change - key
                    if money[key] != 0:
                        money[key] = money[key] - 1
                    else:
                        return False
        return money
