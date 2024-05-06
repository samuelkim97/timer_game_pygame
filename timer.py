import pygame, sys


# general setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

current_time = 0
button_pressed_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            button_pressed_time = pygame.time.get_ticks()
            screen.fill((255, 255, 255))


    current_time = pygame.time.get_ticks()

    if (current_time - button_pressed_time) > 2000:
        screen.fill((0, 0, 0))


    print(f"current time: {current_time}")
    print(f"button pressed time: {button_pressed_time}")

    pygame.display.flip()
    clock.tick(60)