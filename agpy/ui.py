"""Various UI related functions.
"""

from .keyboard import *
from .keycodes import *
from .output import *

import time


def dlg(text: str):
    """Displays a dialog that lets you press the spacebar to repeat, and enter to skip.
    Initially shows the text in speech and Braille, but when space is pressed, only speech.
    """
    output(text)
    while True:
        time.sleep(0.001)
        if key_pressed(K_RETURN):
            break
        if key_pressed(K_SPACE):
            speak(text)
