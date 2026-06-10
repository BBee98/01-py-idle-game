import pygame

def screen():
    return pygame.display

def clock():
    return pygame.time.Clock()

def events():
    return pygame.event.get()

def run(game_scripts):
    pygame.init()
    _running = True
    while _running:
        pydle_events = events()
        for event in pydle_events:
            event_type = event.type
            if event_type == pygame.QUIT:
                _running = False
            print(f"event_type: {event_type}")
            print(f"pygame_QUIT: {pygame.QUIT}")
        _clock = clock()
        _clock.tick(60)
pygame.quit()