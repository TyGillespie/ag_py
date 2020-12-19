"""Game Window opening/closing/handling functions."""

import pygame

from .keyboard import *

from typing import Tuple


def show_window(title: str, size: Touple[int, int] = (200, 200)):
    """Creates a game window."""
    pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    pygame.display.flip()


def flush_window():
    """Flushes the event queue."""
    pygame_queued_events = []
    pygame.event.pump()


def destroy_window():
    """Close the window, and quit Pygame in the process."""
    pygame.quit()
