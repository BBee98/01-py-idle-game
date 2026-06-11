from pygame import display

_screen = display

# initialize

def init():
    _screen.init()
    _visual_screen = screen_size(800, 600)
    screen_fill_with_color(_visual_screen, "black")
    return _screen


def screen_size(width, height):
    return _screen.set_mode((width, height))

def screen_fill_with_color(screen, color):
    screen.fill(color)

def render(screen):
    screen.flip()