if __name__ == '__main__':
    raise Exception(f"Unable to load application file as __main__ level")

def run():
    f = """
Idelette
John
Richard
Greece
Tamara
Samantha
Axel
Gael
Leonel
Sarah
Chuck
Alexandra
Diego
Patrick
Elisa
Isis
Mark
"""
    l = f.split()

    #print(l)

    # Operate the file data
    from aleat3 import Aleatoryous

    r = Aleatoryous("aleatory.roulette", l)
    res = r.first_given(5, repeat=False)      # New since version 0.0.6: no-repetition
    print(res)
    i = input("Done")
