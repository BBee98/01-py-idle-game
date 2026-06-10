import pygame

def quit_game(event_type):
    if event_type == pygame.QUIT:
        pygame.quit()
