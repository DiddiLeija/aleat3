__all__ = ["apps"]

from aleat3.applications import (diceInterface,
                    rouletteWinners,
                    coinWinners,
                    diceMove)

class Transfer:
    def __init__(self):
        self.diceInterface = diceInterface
        self.rouletteWinners = rouletteWinners
        self.coinWinners = coinWinners
        self.diceMove = diceMove

apps = Transfer()
