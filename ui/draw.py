import pygame

font = pygame.font.SysFont(None, 40)

def draw_game(screen, player):
    screen.fill((30, 30, 30))

    money_text = font.render(
        f"Money: {int(player.money)}",
        True,
        (255, 255, 255)
    )

    screen.blit(money_text, (20, 20))