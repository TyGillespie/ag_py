# Initial code written by Stevo.

"""Wraps BGT's timer object in Python.
"""

import time


class TimerException(Exception):
    """Raised when an error occurs.
    Currently does nothing when raised.
    """

    pass


class Timer:
    """Timer object."""

    def __init__(self):
        self.start_time: int = get_current_ms()
        self.running: bool = True
        self.current_time: int = 0

    def restart(self):
        """Restarts the timer backed to 0."""
        self.start_time = get_current_ms()
        self.running = True
        self.current_time = 0

    def pause(self):
        """Pauses the timer, but does not reset it."""
        self.running = False
        self.current_time = get_current_ms() - self.start_time

    def resume(self):
        """Resumes the timer (if it was paused)."""
        self.running = True
        self.start_time = get_current_ms() - self.current_time
        self.current_time = 0

    def get_elapsed(self):
        """Property function for elapsed."""
        if not self.running:
            return int(self.current_time)
        else:
            return int(get_current_ms() - self.start_time)

    def set_elapsed(self, elapsed):
        """Property function to set elapsed."""
        if elapsed < 0:
            raise TimerException("This value must be at least 0")
        self.starttime = get_current_ms() - elapsed
        if not self.running:
            self.current_time = elapsed

    elapsed: property = property(get_elapsed, set_elapsed)


def get_current_ms():
    """Returns the current time in the propper format for the timer."""
    c_time: int = time.time()
    c_time *= 1000
    return c_time
