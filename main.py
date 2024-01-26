import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

pygame.font.init()  # Initialize the font module
font = pygame.font.Font(None, size=160)

buttons = []


class Button:
    def __init__(self, colour, position, size, button_id):
        super().__init__()
        self.id = button_id
        self.image = pygame.Surface(size)

        self.image.fill(colour)  # Replace 'default_color' with a default color if button_id is not found

        self.rect = self.image.get_rect()
        self.rect.topleft = position
        buttons.append(self)

    def highlight(self, mouse_pos):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

        text = str(self.id)
        if text == "clear":
            text = "c"
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, self.rect.topleft)

    def click(self, click_pos):
        action = False
        # checks current mouse position collides with the button
        if self.rect.collidepoint(click_pos):
            # Checks left mouse button
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        return action


Button("red", (0, 100), (100, 100), "clear")

Button("red", (300, 100), (100, 100), "/")
Button("red", (300, 200), (100, 100), "*")
Button("red", (300, 300), (100, 100), "-")
Button("red", (300, 400), (100, 100), "+")
Button("red", (300, 500), (100, 100), "=")

Button("blue", (0, 200), (100, 100), 1)
Button("blue", (100, 200), (100, 100), 2)
Button("blue", (200, 200), (100, 100), 3)
Button("blue", (0, 300), (100, 100), 4)
Button("blue", (100, 300), (100, 100), 5)
Button("blue", (200, 300), (100, 100), 6)
Button("blue", (0, 400), (100, 100), 7)
Button("blue", (100, 400), (100, 100), 8)
Button("blue", (200, 400), (100, 100), 9)
Button("blue", (0, 500), (100, 100), 0)

current_number = ''
expression = []

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
                    if isinstance(button.id, int):
                        current_number += str(button.id)
                    else:
                        if current_number:
                            expression.append(int(current_number))
                            current_number = ''
                        expression.append(button.id)

    for button in buttons:
        button.draw(screen)

    # Render and display the current number
    text_surface = font.render(current_number, True, (255, 255, 255))
    screen.blit(text_surface, (0, 0))

    print(expression)
    if expression:
        if expression[-1] == "clear":
            current_number = ""
            expression.clear()
        elif expression[-1] == "=":
            current_expression = filter(lambda val: val != "=", expression)
            equation_str = ''.join(str(item) for item in current_expression)
            current_number = str(eval(equation_str))
            expression.clear()

    pygame.display.update()
    screen.fill('black')

    clock.tick(60)

pygame.quit()
sys.exit()
