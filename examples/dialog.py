"""Shows a basic text dialog.
"""

import sys
sys.path.append("..")
from agpy import *
sys.path.remove("..")


def main():
    show_window("Dialog test.")
    dlg("Hi!")
    dlg("Test again!")


if __name__ == "__main__":
    main()
