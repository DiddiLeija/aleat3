"""
Use this as a patch if you can't run the
examples correctly:

    from aleat3.applications import apps
    apps.exampleName.run()
"""

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
