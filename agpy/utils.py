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
