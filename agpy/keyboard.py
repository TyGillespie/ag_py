import pygame


pygame_queued_events = []


def key_down(key):
    return pygame.key.get_pressed()[key]


def key_pressed(key):
    kd = key_down(key)
    for event in pygame_queued_events:
        if event.type == pygame.KEYDOWN:
            if event.key == key and kd:
                pygame_queued_events.remove(event)
                return True
            elif event.key == key and not kd:
                pygame_queued_events.remove(event)
                return False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == key:
                return True
            else:
                pygame_queued_events.append(event)
        else:
            pygame_queued_events.append(event)
        return False


def key_released(key):
    for event in pygame_queued_events:
        if event.type == pygame.KEYUP:
            if event.key == key:
                pygame_queued_events.remove(event)
                return True
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == key:
                return True
            else:
                pygame_queued_events.append(event)
        else:
            pygame_queued_events.append(event)
        return False
