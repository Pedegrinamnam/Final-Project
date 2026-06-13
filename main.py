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

running = True

while running:
    for event in pygame.event.get():
        # Запуск
        if event.type == pygame.QUIT:
            running = False
        # Клики
        if click_button.clicked(event):
            player.click()
        # Открыт магаз
        if shop_button.clicked(event):
            shop_open = not shop_open
        # Закрыт магаз
        if shop_open and back_button.clicked(event):
            shop_open = False

    if shop_open:
        draw_shop(
            screen,
            player,
            back_button
        )
    else:
        draw_game(
            screen,
            player,
            click_button,
            shop_button
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

pygame.quit()
