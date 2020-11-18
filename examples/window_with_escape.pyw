"""Shows a basic window that lets you press escape to quit.
"""

import sys

sys.path.append("..")
from agpy import *

sys.path.remove("..")

import time


def main():
    show_window("Agpy example.")
    while True:
        time.sleep(0.001)
        if key_pressed(K_ESCAPE):
            sys.exit()


if __name__ == "__main__":
    main()
