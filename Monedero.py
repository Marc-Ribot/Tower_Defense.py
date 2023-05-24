import math


class Monedero:

    def __init__(self, money):

        self.money = money



    def decrease_money(self, amount):
        if self.money >= amount:
            self.money -= amount

    def increase_money(self, amount):
        self.money += amount

    def get_money(self):
        return self.money
