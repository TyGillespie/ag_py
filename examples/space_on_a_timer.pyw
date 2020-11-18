"""makes you press space on a timer. Also allows you to exit with escape.
Shows the output module as well.
"""

import sys

sys.path.append("..")
from agpy import *

sys.path.remove("..")

import time


def main():
    show_window("Agpy example.")
    space_timer = Timer()
    space_time = 250
    while True:
        time.sleep(0.001)
        if key_pressed(K_SPACE) and space_timer.elapsed >= space_time:
            space_timer.restart()
            speak("Beep!")
        if key_pressed(K_ESCAPE):
            sys.exit()


if __name__ == "__main__":
    main()
