"""Various UI related functions.
"""

from .keyboard import *
from .keycodes import *
from .output import *

import time


def dlg(text: str):
    """Displays a dialog that lets you press the arrows to repeat, and enter to skip."""
    # Todo: Add arrow keys (or even spacebar) to repeat the message.
    output(text)
    while True:
        time.sleep(0.001)
        if key_pressed(K_RETURN):
            break
