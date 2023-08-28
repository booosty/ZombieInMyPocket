from enum import Enum


class State(Enum):
    """
    Different game play states available in game
    """
    STARTED = 1
    STOPPED = 2
    ROTATING = 3
    MOVING = 4
    DRAWING = 5
    COWERING = 6
    BATTLE = 7
    LOST = 8
    WON = 9
