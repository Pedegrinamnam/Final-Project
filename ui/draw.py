import pygame


# Наш криптомайнер
def draw_game(screen, player, click_button, shop_button, rebirth_button):
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
    rebirth_button.draw(screen, font)


# Ларёк
def draw_shop(
    screen,
    player,
    back_button,
    house_button,
    food_button,
    wheel_button,
    friend_button,
    big_house_button
):
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

    house_button.draw(screen, font)
    food_button.draw(screen, font)
    wheel_button.draw(screen, font)
    friend_button.draw(screen, font)
    big_house_button.draw(screen, font)

    back_button.draw(screen, font)


# Перерождения
def draw_rebirth(screen, player, back_button):
    font = pygame.font.SysFont(None, 40)

    screen.fill((15, 15, 15))

    title = font.render(
        "REBIRTH",
        True,
        (255, 255, 255)
    )

    screen.blit(title, (540, 50))

    cost = 10000 * (5 ** player.rebirths)

    text = font.render(
        f"Cost: {cost}",
        True,
        (255, 215, 0)
    )

    screen.blit(text, (500, 250))

    mult = font.render(
        f"Multiplier: x{player.get_multiplier():.2f}",
        True,
        (255, 255, 255)
    )

    screen.blit(mult, (450, 320))

    back_button.draw(screen, font)