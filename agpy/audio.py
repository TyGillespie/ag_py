"""Audio playing functions."""

import playsound

import winsound
import threading

beep_thread: threading.Thread = None


def play_sound(file_name: str, wait: bool = False):
    """Plays an audio file."""
    flag: bool = False
    if wait:
        flag = True
    playsound.playsound(file_name, flag)


def beep(freq: int, length: int):
    """Beeps a tone.
    Currently sleeps the thread (need a way around this, maybe run it in it's own thread)?
    """
    global beep_thread
    if beep_thread is None:
        beep_thread = threading.Thread(
            target=lambda: winsound.Beep(freq, length)
        ).start()
    else:
        beep_thread.start()
