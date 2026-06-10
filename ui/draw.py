import pygame

def draw_game(screen, player, click_button):
    font = pygame.font.SysFont(None, 40)

    screen.fill((30, 30, 30))

    coins_text = font.render(
        f"Coins: {player.money}",
        True,
        (255, 215, 0)
    )

    screen.blit(coins_text, (20, 20))

    click_button.draw(screen, font)