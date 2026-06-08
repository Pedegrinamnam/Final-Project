import pygame

from player import Player
from ui.button import Button

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

player = Player()

click_button = Button(
    500, 250,
    250, 250,
    "HAMSTER"
)

font = pygame.font.SysFont(None, 40)

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if click_button.clicked(event):
            player.click()

    screen.fill((30, 30, 30))

    click_button.draw(screen, font)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()