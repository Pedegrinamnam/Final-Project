import pygame

from player import Player
from ui.button import Button
from ui.draw import draw_game

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

player = Player()

click_button = Button(
    500, 250,
    250, 250,
    "HAMSTER"
)

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if click_button.clicked(event):
            player.click()

    draw_game(screen, player, click_button)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
