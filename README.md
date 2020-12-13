# ag_py

An audio game engine written in Python.

## Features.

* Keyboard handling that wraps Pygame.
* Basic window support.
* UI support (currently only dialogs).
* Basic audio support (wave files).
* Different options for outputting to a screen reader (wraps Cytolk).

## Contributing.

Feel free to contribute, either with Pole Requests or Issues. If using PRs, I ask that you format for PEP-8. If not, I can do it, but it would be appriciated. There is even a Bat file to do it for you. Also please make sure your code runs before contributing it. Also browse open issues/PRs before opening a new one.

## Changes

### 0.11

* Beeps now occur in a thread.
* speak now only speaks.
* The output function silences automatically. The silence function still exists if needed, though.
* Fixed some typos.
* The space_on_a_timer example now beeps, not just says "Beep!".
