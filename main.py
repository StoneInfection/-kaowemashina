from coffee_base import Currency
from money_coffee_machine import MoneyCoffeeMachine
from service import CoffeSrvice


class Interface:
    def __init__(self):
        self.srvice = CoffeSrvice()

    def coffe(self):
        coffe = input("выберити кофе: Капучино-1, Латте-2, Флэт-уайт-3, Американо-4, Макиато-5, Фраппе-6: ")
        amount = self.srvice.get_coffe(coffe)
        self.calculating_balance(amount)

    def calculating_balance(self, amount):
        balance = 0
        while amount > balance:
            users_purse = int(input(f"стоимость кофе - {amount}, ваш баланс - {balance}: "))
            currency = self.srvice.get_currency()
            if users_purse in currency:
                balance = self.srvice.calculating_balance(users_purse, balance)
            else:
                print(f"извените , но такую валюту мы не принимаем, мы принимаем только {Currency().currency()}")
        self.create_coffe()
        if balance > amount:
            self.calculating_change(balance, amount)
        self.coffe()

    def create_coffe(self):
        cup = input("поставте стаканчик где будет наливаться ваше кофе: ")
        if cup == "yes":
            print("наливаем кофе")
            print("наливаем молоко")
            print("ваш напиток готов")
        else:
            self.create_coffe()

    def calculating_change(self, balance: int, amount: int):
            change = self.srvice.calculating_change(amount, balance)
            money = MoneyCoffeeMachine().subtract_money(change)
            if not money:
                print("ивените но в  даный момент я не могу выдать вам сдачу , обратитесь к менаджеру,"
                      f" ваша сдача должна состовлять: {change}")
            else:
                print("осталось денег", money)
                print(f"ваша сдача {change}")


Interface().coffe()
