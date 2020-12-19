"""Keyboard handling."""

import pygame


pygame_queued_events = []


def key_down(key: int) -> bool:
    """Function to tell if a key is held down."""
    return pygame.key.get_pressed()[key]


def key_pressed(key: int) -> bool:
    """Determines if the given keycode is being pressed."""
    kd = key_down(key)
    # First, handle the queued events, if any.
    for event in pygame_queued_events:
        if event.type == pygame.KEYDOWN:
            if event.key == key and kd:
                pygame_queued_events.remove(event)
                return True
            elif event.key == key and not kd:
                pygame_queued_events.remove(event)
                return False
    # Now, handle normal events.
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == key:
                return True
            else:
                pygame_queued_events.append(event)
        else:
            pygame_queued_events.append(event)
        return False


def key_released(key: int) -> bool:
    """Determines if the given key is released."""
    # Handle the queued keys."""
    for event in pygame_queued_events:
        if event.type == pygame.KEYUP:
            if event.key == key:
                pygame_queued_events.remove(event)
                return True
    # Time to handle normal events! Weeeee!
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == key:
                return True
            else:
                pygame_queued_events.append(event)
        else:
            pygame_queued_events.append(event)
        return False
