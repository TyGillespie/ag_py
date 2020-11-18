"""Audio playing functions."""

import playsound

import winsound


def play_sound(file_name: str, wait: bool = False):
    """Plays an audio file."""
    flag: bool = False
    if wait:
        flag = True
    playsound.playsound(file_name, flag)


def beep(freq: int, lentgh: int):
    """Beeps a tone.
    Currently sleeps the thread (need a way around this, maybe run it in it's own thread)?
    """
    winsound.Beep(freq, length)
