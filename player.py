class Player:
    def __init__(self):
        self.money = 0

        self.total_clicks = 0

        self.rebirths = 0

        self.upgrades = {
            "Домик": 0,
            "Кормушка": 0,
            "Колесо": 0,
            "Особняк": 0
        }

    def get_multiplier(self):
        return 1.5 ** self.rebirths

    def click(self):
        self.money += 1 * self.get_multiplier()
        self.total_clicks += 1

    def get_income(self):
        return (
            self.upgrades["Домик"] * 1 +
            self.upgrades["Кормушка"] * 5 +
            self.upgrades["Колесо"] * 20 +
            self.upgrades["Особняк"] * 100
        ) * self.get_multiplier()

    def update(self, dt):
        self.money += self.get_income() * dt

    def rebirth(self):
        cost = 100000 * (5 ** self.rebirths)

        if self.money >= cost:
            self.money = 0
            self.rebirths += 1

            for upgrade in self.upgrades:
                self.upgrades[upgrade] = 0
