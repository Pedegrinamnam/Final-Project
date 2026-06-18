import pygame



def get_rebirth_cost(rebirths):
    return 10000 * (5 ** rebirths)

def can_rebirth(player):
    return player.money >= get_rebirth_cost(player.rebirths)

def rebirth(self):
    cost = 10000 * (5 ** self.rebirths)

    if self.money >= cost:
        self.money = 0
        self.rebirths += 1

        for upgrade in self.upgrades:
            self.upgrades[upgrade] = 0