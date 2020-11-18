"""Audio playing functions."""

import winsound


def play_sound(file_name: str, wait: bool = False):
    """Plays an audio file.
    Currently only supports wave files.
    """
    flags: int = 0
    if not wait:
        flags = winsound.SND_ASYNC
    winsound.PlaySound(file_name, flags)


def beep(freq: int, lentgh: int):
    """Beeps a tone.
    Currently sleeps the thread (need a way around this, maybe run it in it's own thread)?
    """
    winsound.Beep(freq, length)
