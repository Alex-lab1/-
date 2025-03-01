import pygame

# Инициализация Pygame
pygame.init()

# Размеры окна
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Character Movement")

cursor = pygame.image.load("data/cursor.png").convert_alpha()  #Замените character.png на ваше изображение

cursor = pygame.transform.scale(cursor, (50, 50)) # Пример масштабирования

x, y = 0, 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 0.1
    if keys[pygame.K_RIGHT]:
        x += 0.1
    if keys[pygame.K_UP]:
        y -= 0.1
    if keys[pygame.K_DOWN]:
        y += 0.1

    screen.fill((255, 255, 255))  # Белый фон
    screen.blit(cursor, (x, y))

    pygame.display.flip()

pygame.quit()
