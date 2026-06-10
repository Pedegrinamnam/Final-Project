import pygame

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, screen, font):
        pygame.draw.rect(screen, (80, 80, 80), self.rect)

        text = font.render(self.text, True, (255, 255, 255))
        screen.blit(
            text,
            text.get_rect(center=self.rect.center)
        )

    def clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and self.rect.collidepoint(event.pos)
        )
