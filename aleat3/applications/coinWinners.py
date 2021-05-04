"Play with Heads or Tails and receive if you won or not."

if __name__ == '__main__':
    raise Exception(f"Unable to load application file as __main__ level")

def run():
    from aleat3 import Aleatoryous, coinToBinary
    from aleat3.output.colored import output_bright

    coin = Aleatoryous()
    side = coin.single()

    if coinToBinary(side) == 1:
        output_bright("You voted for Head")
    else:
        output_bright("You voted for Tails")

    if coinToBinary(coin.single()) == coinToBinary(side):
        output_bright("You win!!!")
    else:
        output_bright("You lose!!!")
    e = input("\nDone")
