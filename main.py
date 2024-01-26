import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

buttons = []


class Button():
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        buttons.append(self)

    def highlight(self, mouse_pos):
        pass

    def click(self, mouse_click):
        pass


Button((400, 400), (20, 20))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            for button in buttons:
                button.highlight(event.pos)

    buttons.draw(screen)

    pygame.display.update()
    screen.fill('black')

    clock.tick(60)

pygame.quit()
sys.exit()
