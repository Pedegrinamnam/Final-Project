import pygame

from player import Player
from ui.draw import draw_game, draw_shop, draw_rebirth
from ui.button import Button

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

player = Player()
shop_open = False
rebirth_open = False

# Сам хомяк (Хомячная кнопка)
click_button = Button(
    500, 250,
    250, 250,
    "HAMSTER"
)
# Сам магазин (Магазинная кнопка)
shop_button = Button(
    1060, 650,
    200, 50,
    "Shop"
)
# Кнопка выхода из магазина (Выходная кнопка)
back_button = Button(
    20, 650,
    200, 50,
    "Back"
)
# Кнопка перерождения (Перерожденная кнопка)
rebirth_button = Button(
    840, 650,
    200, 50,
    "REBIRTH"
)
# Кнопка выхода из перерождения (Выходно-перерожденная кнопка)
rebirth_back_button = Button(
    20, 650,
    200, 50,
    "BACK"
)

house_button = Button(400, 180, 300, 50, "Дом - 10$")
food_button = Button(400, 250, 300, 50, "Хавалка - 500$")
wheel_button = Button(400, 320, 300, 50, "Колесо - 250$")
friend_button = Button(400, 460, 300, 50, "Друг - 5000$")
big_house_button = Button(400, 390, 320, 50, "ДомПобольше - 10000$")

running = True

while running:
    for event in pygame.event.get():
        # Улучшения в магазе
        if shop_open:
            # Улучшения в магазе
            if shop_open:
                # Дом
                if house_button.clicked(event):
                    player.buy_upgrade("Дом")
                # Хавалка
                if food_button.clicked(event):
                    player.buy_upgrade("Хавалка")
                # Колесо
                if wheel_button.clicked(event):
                    player.buy_upgrade("Колесо")
                # ДомПобольше
                if big_house_button.clicked(event):
                    player.buy_upgrade("ДомПобольше")
                # Друн
                if friend_button.clicked(event):
                    player.buy_upgrade("Друг")
        # Запуск
        if event.type == pygame.QUIT:
            running = False
        # Клики
        if not shop_open and click_button.clicked(event):
            player.click()
        # Открыть магаз
        if not shop_open and shop_button.clicked(event):
            shop_open = True
        # Закрыть магаз
        if shop_open and back_button.clicked(event):
            shop_open = False
        # Открыть перерождение
        if not shop_open and not rebirth_open and rebirth_button.clicked(event):
            rebirth_open = True
        # Открыть перерождение
        if not shop_open and not rebirth_open and rebirth_button.clicked(event):
            rebirth_open = True
        # Закрыть перерождение
        if rebirth_open and rebirth_back_button.clicked(event):
            rebirth_open = False

    if shop_open:
        draw_shop(
            screen,
            player,
            back_button,
            house_button,
            food_button,
            wheel_button,
            friend_button,
            big_house_button
        )
    elif rebirth_open:
        draw_rebirth(
            screen,
            player,
            rebirth_back_button
        )

    else:
        draw_game(
            screen,
            player,
            click_button,
            shop_button,
            rebirth_button
        )

    pygame.display.flip()
    dt = clock.tick(60) / 1000
    player.update(dt)

pygame.quit()

pygame.quit()
