import pygame

from .keyboard import *


def show_window(title, size=(200, 200)):
    pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    pygame.display.flip()


def flush_window():
    pygame_queued_events = []
    pygame.event.pump()


def destroy_window():
    pygame.quit()
