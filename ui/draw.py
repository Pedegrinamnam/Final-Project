import pygame

def draw_game(screen, player, click_button, shop_button):
    font = pygame.font.SysFont(None, 40)

    screen.fill((30, 30, 30))

    money_text = font.render(
        f"MONEY: {int(player.money)}",
        True,
        (255, 215, 0)
    )
    screen.blit(money_text, (20, 20))

    click_button.draw(screen, font)
    shop_button.draw(screen, font)


def draw_shop(screen, player, back_button):
    font = pygame.font.SysFont(None, 40)

    screen.fill((20, 20, 20))

    title = font.render(
        "SHOP",
        True,
        (255, 255, 255)
    )

    screen.blit(title, (570, 50))

    money_text = font.render(
        f"MONEY: {int(player.money)}",
        True,
        (255, 215, 0)
    )

    screen.blit(money_text, (20, 20))

    upgrades = [
        "Дом - 10$",
        "Хавалка - 50$",
        "Колесо - 250$",
        "ДомПобольше - 1000$"
    ]

    y = 180

    for upgrade in upgrades:
        text = font.render(
            upgrade,
            True,
            (255, 255, 255)
        )

        screen.blit(text, (450, y))

        y += 60

    back_button.draw(screen, font)