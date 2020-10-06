# ag_py
An audio game engine written in Python.
## Usage.
from agpy import *

import time
import sys


agpy.show_window("Test game.")
while True:
    time.sleep(0.005)
    if key_pressed(K_ESCAPE):
        sys.exit()
