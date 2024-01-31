class CoffeeBase:
    def cost_coffee(self):
        return {"1": 100, "2": 140, "3": 160, "4": 150, "5": 200, "6": 195, }


class Currency:
    def currency(self):
        return [5, 10, 50, 100, 200, 500]


class MoneyCoffeeMachineBase:
    def money_coffee_machine(self):
        return {500: 1000, 200: 1000, 100: 1000, 50: 0, 10: 1000, 5: 0}
