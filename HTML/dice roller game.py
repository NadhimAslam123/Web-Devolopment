import pygame
import random

pygame.init()

screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Dice Roller")

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 50)
roll_button = pygame.Rect(100, 120, 100, 40)
dice_result = 0

def roll_dice():
    return random.randint(1, 6)

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.rect(screen, GRAY, roll_button)
    text = font.render("Roll", True, BLACK)
    screen.blit(text, (roll_button.x + 15, roll_button.y + 5))

    if dice_result != 0:
        result_text = font.render(f"{dice_result}", True, BLACK)
        screen.blit(result_text, (140, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if roll_button.collidepoint(event.pos):
                dice_result = roll_dice()

    pygame.display.update()

pygame.quit()