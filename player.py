import pygame
from upgrades import UPGRADES

class Player:
    def __init__(self):
        self.money = 0
        self.total_clicks = 0
        self.rebirths = 0
        self.upgrades = {
            "Дом": 0,
            "Хавалка": 0,
            "Колесо": 0,
            "ДомПобольше": 0
        }

        def buy_upgrade(self, name, cost):
            if self.money >= cost:
                self.money -= cost
                self.upgrades[name] += 1
                return True

            return False
# Множитель деняк
    def get_multiplier(self):
        return 1.5 ** self.rebirths
# Тапы
    def click(self):
        self.money += 1 * self.get_multiplier()
        self.total_clicks += 1
# Заработок с крипты
    def get_income(self):
        return (
            self.upgrades["Дом"] * 1 +
            self.upgrades["Хавалка"] * 5 +
            self.upgrades["Колесо"] * 20 +
            self.upgrades["ДомПобольше"] * 100
        ) * self.get_multiplier()
# Апдейты
    def update(self, dt):
        self.money += self.get_income() * dt
# Стоимость перерождения
    def rebirth(self):
        cost = 10000 * (5 ** self.rebirths)
        if self.money >= cost:
            self.money = 0
            self.rebirths += 1
            for upgrade in self.upgrades:
                self.upgrades[upgrade] = 0
