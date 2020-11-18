"""Shows a basic window that lets you press escape to quit.
"""

import sys

sys.path.append("..")
from agpy.window import *
from agpy.keyboard import *
from agpy.keycodes import *
from agpy.utils import *

sys.path.remove("..")

import time


def main():
    show_window("Agpy example.")
    while True:
        time.sleep(0.001)
        if key_pressed(K_ESCAPE):
            quit()


if __name__ == "__main__":
    main()
