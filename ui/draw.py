import pygame


# Наш криптомайнер
def draw_game(
    screen,
    player,
    click_button,
    shop_button,
    rebirth_button,
    hamster_image,
    coins_image,
    coins
):
    font = pygame.font.SysFont(None, 40)

    screen.fill((30, 30, 30))

    # Монетки, которые делают динь-динь
    for coin in coins:
        screen.blit(
            coins_image,
            (coin["x"], coin["y"])
        )

    money_text = font.render(
        f"MONEY: {int(player.money)}",
        True,
        (255, 215, 0)
    )

    screen.blit(money_text, (20, 20))

    # Хомяк
    screen.blit(
        hamster_image,
        click_button.rect
    )

    # Кнопки
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
    big_house_button,
    rules_image
):
    font = pygame.font.SysFont(None, 40)

    screen.fill((20, 20, 20))

    # Рулс Каард
    screen.blit(rules_image, (900, 350))


    house_button.draw(screen, font)
    food_button.draw(screen, font)
    wheel_button.draw(screen, font)
    friend_button.draw(screen, font)
    big_house_button.draw(screen, font)

    back_button.draw(screen, font)


# Перерождения
def draw_rebirth(
    screen,
    player,
    back_button,
    rebirth_confirm_button,
    black_hole_image):
    font = pygame.font.SysFont(None, 40)

    screen.fill((15, 15, 15))

    # Чёрная дыра которая делает оаоаоаОАОАОАОАОАОАОАООАООАОАОАОАОАОАОАОАООААОАОАОАОАОАОАОАОАОАОАООАОАОААААААААААА
    screen.blit(
        black_hole_image,
        (-50, -100)
    )

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

    rebirth_confirm_button.draw(screen, font)