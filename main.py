import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = pygame.Rect(100, 100, 40, 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]: player.x += 5
    if keys[pygame.K_LEFT]:  player.x -= 5

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (100, 200, 255), player)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()