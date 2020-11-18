"""Utility related functions.
"""

import sys
import os
import ctypes

import pygame

from .window import *


def quit():
    """Shuts down ag_py the correct way."""
    destroy_window()
    pygame.quit()
    sys.exit()


def is_admin() -> bool:
    """Determains if the user is running your game as admin."""
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0


def percent(n1: int, n2: int) -> bool:
    """Finds the percentage of n1 out of n2.
    For example, if n1 was 5, and n2 was 10, it would return 50.
    """
    return (n1 / n2) * 100


def generate_string(length: int) -> str:
    """Generates a random string of a given lentgh."""
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    final_string = ""
    for i in range(length):
        final_string += symbols[random.randint(0, len(symbols) - 1)]
    return final_string
