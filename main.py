from service import CoffeSrvice


class Interface:

    def coffe(self):
        coffe = input("выберити кофе: Капучино-1, Латте-2, Флэт-уайт-3, Американо-4, Макиато-5, Фраппе-6: ")
        amount = CoffeSrvice().get_coffe(coffe)
        self.balance(amount)

    def balance(self, amount):
        balance = 0
        while amount > balance:
            users_purse = int(input(f"стоимость кофе - {amount}, ваш баланс - {balance}: "))
            currency = CoffeSrvice().get_currency()
            if users_purse in currency:
                balance = CoffeSrvice().balance(users_purse, balance)
            else:
                print("извените , но такую валюту мы не принимаем, мы принимаем только 5, 10, 50, 100, 200, 500")
        self.create_coffe()
        if balance > amount:
            self.change(balance, amount)

    def create_coffe(self):
        cup = input("поставте стаканчик где будет наливаться ваше кофе: ")
        if cup == "yes":
            print("наливаем кофе")
            print("наливаем молоко")
            print("ваш напиток готов")
        else:
            self.create_coffe()

    def change(self, balance: int, amount: int):
            change = CoffeSrvice().change(amount, balance)
            print(f"ваша сдача {change}")


Interface().coffe()
