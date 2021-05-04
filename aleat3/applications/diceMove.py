"Movement choice with aleatory.dice"

if __name__ == '__main__':
    raise Exception(f"Unable to load application file as __main__ level")

def run():
    #import time
    from aleat3 import Aleatoryous
    from aleat3.output.colored import (output_bright,
                                       output_green,
                                       output_red)
    output_bright("""Welcome to DiceMove!

Here, you must defeat a computer syntax by using our Aleatoryous dice.
Both dices will roll and the first one who gets 50 as a result will win!

(If the program pauses, press Enter to continue)\n""")
    i = input()
    a = Aleatoryous("aleatory.dice")
    b = Aleatoryous("aleatory.dice")
    aa = 0
    bb = 0
    for e in range(50):
        e = e + 1
        output_bright("Move %s:" % e)
        _a = a.single()
        _b = b.single()
        aa += _a
        bb += _b
        output_green("YOUR MOVE: %s" % _a)
        output_red("COMPUTER MOVE: %s" % _b)
        if aa >= 50:
            output_bright("YOU WON WITH %s POINTS!" % aa)
            break
        elif bb >= 50:
            output_bright("YOU LOSE!")
            break
        else:
            output_bright("""The game keeps going with points:

- YOU: %s
- COMPUTER: %s""" % (aa, bb))
            i = input()
