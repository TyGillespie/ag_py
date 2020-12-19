"""Wraps Cytolk for output.
"""

from cytolk import tolk


# Initialize the system upon import.
tolk.load()


def speak(text: str):
    """Speak a string of text."""
    tolk.speak(text)


def braille(text: str):
    """Braille a string of text to the screen reader."""
    tolk.braille(text)


def output(text):
    """Output a string to both Braille and Speech.
    More unreliable, as one will most likely take
    priority (this is a Tolk/Screen Reader issue).
    """
    silence()
    tolk.output(text)


def silence():
    """Silence the screen reader (if currently speaking)."""
    tolk.silence()
