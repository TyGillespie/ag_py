"""Audio playing functions."""

import playsound

import ctypes
import threading


# kernel32 DLL handle.
kernel32 = ctypes.windll.kernel32


def play_sound(file_name: str, wait: bool = False):
    """Plays an audio file."""
    flag: bool = False
    if wait:
        flag = True
    playsound.playsound(file_name, flag)


def beep(freq: int, length: int, threaded: bool = True):
    """Beeps a tone through the PC speaker."""
    if threaded:
        beep_thread: threading.Thread = threading.Thread(
            target=lambda: kernel32.Beep(freq, length)
        ).start()
    else:
        kernel32.Beep(freq, length)
