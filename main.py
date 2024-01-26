import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()

buttons = []


class Button:
    def __init__(self, position, size, button_id):
        super().__init__()
        self.id = button_id
        self.image = pygame.Surface(size)
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        buttons.append(self)

    def highlight(self, mouse_pos):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def click(self, click_pos):
        action = False
        # checks current mouse position collides with the button
        if self.rect.collidepoint(click_pos):
            # Checks left mouse button
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        return action


Button((300, 0), (100, 100), "/")
Button((300, 100), (100, 100), "x")
Button((300, 200), (100, 100), "-")
Button((300, 300), (100, 100), "+")
Button((300, 400), (100, 100), "=")

Button((0, 100), (100, 100), 1)
Button((100, 100), (100, 100), 2)
Button((200, 100), (100, 100), 3)
Button((0, 200), (100, 100), 4)
Button((100, 200), (100, 100), 5)
Button((200, 200), (100, 100), 6)
Button((0, 300), (100, 100), 7)
Button((100, 300), (100, 100), 8)
Button((200, 300), (100, 100), 9)
Button((0, 400), (100, 100), 0)

pressed = []
expression = ""
current_number = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            for button in buttons:
                button.highlight(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.click(event.pos):
                    pressed.append(button.id)

    for button in buttons:
        button.draw(screen)

    pygame.display.update()
    screen.fill('black')

    clock.tick(60)

pygame.quit()
sys.exit()
