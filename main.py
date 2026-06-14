import pygame

from player import Player
from ui.draw import draw_game, draw_shop
from ui.button import Button

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

player = Player()
shop_open = False
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
# Кнопка выхода из магазина
back_button = Button(
    20, 650,
    200, 50,
    "Back"
)

house_button = Button(400, 180, 300, 50, "Дом - 10$")
food_button = Button(400, 250, 300, 50, "Хавалка - 50$")
wheel_button = Button(400, 320, 300, 50, "Колесо - 250$")
big_house_button = Button(400, 390, 300, 50, "ДомПобольше - 1000$")
friend_button = Button(400, 460, 300, 50, "Друг - 1000$")

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

    if shop_open:
        draw_shop(
            screen,
            player,
            back_button,
            house_button,
            food_button,
            wheel_button,
            big_house_button,
            friend_button
        )
    else:
        draw_game(
            screen,
            player,
            click_button,
            shop_button
        )

    pygame.display.flip()
    dt = clock.tick(60) / 1000
    player.update(dt)

pygame.quit()

pygame.quit()
