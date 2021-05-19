"""
Use this as a patch if you can't run the
examples like this (take an 'exampleName' example):

    from aleat3.applications.exampleName import run
    run()

If you can't, use the 'apps' object that packaged all
the registered examples:

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
