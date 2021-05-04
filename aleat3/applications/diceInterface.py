"An example of using aleatory.dice in Tkinter interfaces."

if __name__ == '__main__':
    raise Exception(f"Unable to load application file as __main__ level")

from aleat3 import Aleatoryous
from tkinter import *

__all__ = ["run"]
__author__ = "Diego Ramirez (dr01191115@gmail.com) @DiddiLeija"

class diceInterface:
    "A simple interface that uses aleatory.dice mode and Tkinter library."

    def __init__(self, root, title="aleatory.dice: Tkinter example"):
        self.root = root
        self.root.title(title)
        self.root.maxsize(500, 110)
        self.dice_s = Aleatoryous("aleatory.dice")
        self.principal()

    def principal(self):
        self.frame = Frame(self.root)
        self.frame.grid()
        self.dice_i = Label(self.frame,
                            text="6",
                            font=("Times", "50", "bold"),
                            fg="gray",
                            bg="white",
                            bd=1,
                            width=5)
        self.dice_i.grid(row=0, column=0)
        self.start = Button(self.frame,
                            text="Roll Dice",
                            fg="green",
                            bg="white",
                            command=self.roll_dice,
                            anchor="s")
        self.start.grid(row=1, column=0)
        self.info = Label(self.frame,
                          text="""Use the aleatory.dice syntax
for creating dice games easier.
If you want, use a dice image instead of tkinter.Label()""",
                          fg="black")
        self.info.grid(row=0, column=1)
        self.exit = Button(self.frame,
                           text="Close example",
                           fg="red",
                           bg="white",
                           command=self.root.quit,
                           anchor="s")
        self.exit.grid(row=1, column=1)

    def roll_dice(self):
        tot = str(self.dice_s.single())
        self.dice_i.config(text=tot, fg="blue")


def run(title="aleatory.dice: Tkinter example"):
    _r = Tk()
    _inst = diceInterface(_r, title)
    _r.mainloop()
    i = input("Done")
