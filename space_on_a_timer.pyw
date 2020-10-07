from agpy import *

import winsound
import time
import sys


def main():

    show_window("Agpy example.")
    space_timer = Timer()
    space_time = 250
    while True:
        time.sleep(0.005)
        if key_pressed(K_SPACE) and space_timer.elapsed >= space_time:
            space_timer.restart()
            winsound.Beep(250, 250)
        if key_pressed(K_ESCAPE):
            sys.exit()


if __name__ == "__main__":
    main()
