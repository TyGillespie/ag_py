"""Wraps Cytolk for output.
"""

from cytolk import tolk


tolk.load()


def speak(text: str):
    """Speak a string of text."""
    tolk.output(text)


def braille(text: str):
    """Braille a string of text to the screen reader."""
    tolk.braille(text)


def output(text):
    """Output a string to both Braille and Speech.
    More unreliable, as one will most likely take
    priority (this is a Tolk/Screen Reader issue).
    """
    tolk.output(text)


def slience():
    """Silence the screen reader (if currently speaking).
    This should be called before output() for more reliability.

    Todo: Call this function inside output() itself.
    """
    tolk.silence()
