# Initial code written by Stevo.

import time


class TimerException(Exception):
    pass


class Timer:
    def __init__(self):
        self.start_time = get_current_ms()
        self.running = True
        self.current_time = 0

    def restart(self):
        self.start_time = get_current_ms()
        self.running = True
        self.current_time = 0

    def pause(self):
        self.running = False
        self.current_time = get_current_ms() - self.start_time

    def resume(self):
        self.running = True
        self.start_time = (get_current_ms() - self.current_time)
        self.current_time = 0

    def get_elapsed(self):
        if self.running == False:
            return int(self.current_time)
        else:
            return int(get_current_ms()-self.start_time)

    def set_elapsed(self, elapsed):
        if elapsed < 0:
            raise TimerException("This value must be at least 0")
        self.starttime = (get_current_ms() - elapsed)
        if self.running == False:
            self.current_time = elapsed
    elapsed = property(get_elapsed, set_elapsed)


def get_current_ms():
    ctime = time.time()
    ctime *= 1000
    return ctime
