from enum import Enum


class State(Enum):
    STARTED = 1
    STOPPED = 2
    ROTATING = 3
    MOVING = 4
    DRAWING = 5
    LOST = 6
    WON = 7
