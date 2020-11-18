"""Various UI related functions.
"""

from .keyboard import *
from .keycodes import *
from .output import *

import time


def dlg(text: str):
    """Displays a dialog that lets you press the arrows to repeat, and enter to skip."""
    # Todo: Add Braille support, for the initial dialog. Not for repeating.
    speak(text)
    while True:
        time.sleep(0.001)
        if (
            key_pressed(K_UP)
            or key_pressed(K_DOWN)
            or key_pressed(K_LEFT)
            or key_pressed(K_RIGHT)
        ):
            speak(text)
        if key_pressed(K_RETURN):
            break
