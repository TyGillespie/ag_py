from agpy import *

import time
import sys


def main():
    show_window("Agpy example.")
    while True:
        time.sleep(0.005)
        if key_pressed(K_ESCAPE):
            sys.exit()


if __name__ == "__main__":
    main()
