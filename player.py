import pygame
from upgrades import upgrades

class Player:
    def __init__(self):
        self.money = 0
        self.total_clicks = 0
        self.rebirths = 0
        self.upgrades = {
            "Дом": 0,
            "Хавалка": 0,
            "Колесо": 0,
            "ДомПобольше": 0,
            "Друг": 0
        }

    def buy_upgrade(self, name):
        from upgrades import upgrades

        cost = upgrades[name]["cost"]
        limit = upgrades[name]["limit"]

        if self.money < cost:
            return False

        if limit is not None and self.upgrades[name] >= limit:
            return False

        self.money -= cost
        self.upgrades[name] += 1

        return True

# Множитель деняк
    def get_multiplier(self):
        return 1.5 ** self.rebirths
    # Сила клика
    def get_click_power(self):
        return (
        1 +
        self.upgrades["Дом"] * 1 +
        self.upgrades["Хавалка"] * 10 +
        self.upgrades["Колесо"] * 50 +
        self.upgrades["ДомПобольше"] * 100
        )
# Тапы
    def click(self):
        self.money += self.get_click_power() * self.get_multiplier()
        self.total_clicks += 1
# Заработок с крипты
    def get_income(self):
        return (
                self.upgrades["Друг"] * 1
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
