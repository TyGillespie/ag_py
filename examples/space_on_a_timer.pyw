"""makes you press space on a timer. Also allows you to exit with escape.
Shows the output module as well.
"""

import sys

sys.path.append("..")
from agpy.keyboard import *
from agpy.keycodes import *
from agpy.window import *
from agpy.timer import *
from agpy.utils import *
from agpy.audio import *

sys.path.remove("..")

import time


def main():
    show_window("Agpy example.")
    space_timer: Timer = Timer()
    space_time: int = 250
    while True:
        time.sleep(0.001)
        if key_pressed(K_SPACE) and space_timer.elapsed >= space_time:
            space_timer.restart()
            beep(500, 100)
        if key_pressed(K_ESCAPE):
            quit()


if __name__ == "__main__":
    main()
