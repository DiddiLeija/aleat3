# The whole syntax of Aleatoryous3

__all__ = ["InitError",
           "Aleatoryous",
           "coinToBinary",
           "coinToBool"]


import random

if __name__ != "__main__":
    from aleat3.output import init_errors as IE, colored as _color
else:
    from output import init_errors as IE, colored as _color


class InitError(TypeError):
    pass


"New since 0.1.5: Cleaner operations"
class Aleatoryous:
    "New since 0.0.4: Some variables deleted or recycled"
    "New since 0.0.9: More variables recycled"
    tot = 0
    #__cache = ["Coin", "Dice", "Roulette"]
    __mode = ""
    parser = ""
    lst = []
    __methods = ["__init__",
                 "__len__",
                 "__dir__",
                 "refresh",
                 "single",
                 "first_5",
                 "first_10",
                 "first_50",
                 "first_100",
                 "first_given",
                 "getmode",
                 "changemode"]
    dict = {}
    __it = 0

    def __init__(self, mode="aleatory.coin", extras=None):
        if mode == "aleatory.coin":
            self.__mode = "Coin"
            self.__it = 2
        elif mode == "aleatory.dice":
            self.__mode = "Dice"
            self.__it = 6
        elif mode == "aleatory.roulette":
            self.__mode = "Roulette"
            if extras is not None:
                self.parser = extras
            if not isinstance(self.parser, type([1, 2, 3])):
                raise InitError(IE.parameter_bug())
            else:
                pass
            for i in range(len(self.parser)):
                self.it = i + 1
                self.dict[self.parser[i]] = self.it
            self.__it = len(self.parser)
        else:
            raise InitError(IE.modal_bug())
        #self.cache = ""
        self.__modetye = mode
        self.parser = ""


    def refresh(self):
        self.tot = ""
        self.lst = []


    def single(self):
        if self.__mode == "Coin":
            self.tot = random.randint(0, 1)
            if self.tot == 1:
                return "Head"
            elif self.tot == 0:
                return "Tails"
            else:
                return None

        elif self.__mode == "Dice":
            self.tot = random.randint(1, 6)
            return self.tot

        elif self.__mode == "Roulette":
            self.tot = random.randint(1, len(self.dict))
            for k, v in self.dict.items():
                if v == self.tot:
                    self.tot = k
                    break
            return self.tot


    def first_5_basic(self):
        "New since 0.0.6: Faster operations"
        for t in [1, 2, 3, 4, 5]:
            self.lst.append(self.single())


    def first_5(self):
        self.refresh()
        self.first_5_basic()
        return self.lst


    def first_10(self):
        self.refresh()
        "New since 0.2.3: Faster operations"
        for t in range(2):
            self.first_5_basic()
        return self.lst


    def first_50(self):
        self.refresh()
        "New since 0.2.3: Faster operations"
        for t in range(10):
            self.first_5_basic()
        return self.lst


    def first_100(self):
        self.refresh()
        "New since 0.2.3: Faster operations"
        for t in range(20):
            self.first_5_basic()
        return self.lst


    def first_given(self, how, /, repeat=True):
        "New since 0.0.6: You can iterate with no repetition"
        "New since 0.0.7: No-repetition operation corrected"
        "New since 0.1.3: No-repetition operation corrected"
        self.refresh()
        if not isinstance(how, type(1)):
            raise SyntaxError(f"Expected integers, %s given" % type(how))
        else:
            if self.__mode == "Coin" and repeat is False:
                raise SyntaxError(f"'No-repetition' feature is not available for 'aleatory.dice' objects")
            if not repeat and how > self.__it:
                raise SyntaxError(f"Cannot give more than %s iterations without repetitions." % self.__it)
        if repeat is True:
            for time in range(how):
                self.lst.append(self.single())
        elif repeat is False:
            while len(self.lst) != how:
                possible = self.single()
                if possible in self.lst:
                    continue
                self.lst.append(possible)
        else:
            raise SyntaxError(f"At parameter 'repeat', you must enter True or False, not %s" % repeat)
        return self.lst


    def getmode(self):
        "New since 0.0.3: get the private mode."
        self.refresh()
        return self.__modetype


    def changemode(self, mode, extras=None):
        "New since 0.0.3: restart the object with a new mode."
        self.__init__(mode, extras)

    # Some built-in functions
    def __len__(self):
        return self.__it  # The number of options
    def __dir__(self):
        return self.__methods
    def __str__(self):
        return "Aleatoryous " + self.__modetype


#################################################################################################################################################
def coinToBinary(res):
    if res.strip().lower() == "head":
        return 1
    elif res.strip().lower() == "tails":
        return 0
    else:
        _color.output_red("ERROR: You must enter an aleatory.dice string output for binary conversion. The default value will be set as None.")
        return None

def coinToBool(res):
    "New since 0.0.8: From string to boolean"
    e = coinToBinary(res)
    if e == 1:
        return True
    elif e == 0:
        return False
    else:
        _color.output_red("ERROR: You must enter an aleatory.dice string output for boolean conversion. The default value will be set as None.")


#################################################################################################################################################
"New since 0.1.1: Module test"

def module_test():
    import time
    _color.output_magenta("----Module test: constructor.py----")
    #print("----Module test----\n")
    print("Testing module...\n")

    try:
        print("Testing objects...")
        time.sleep(0.7)
        try:
            print("-Testing object 'aleat3.Aleatoryous'...")
            i = Aleatoryous()
            i.changemode("aleatory.roulette", [1, 2, 3])
            i.changemode("aleatory.dice")
            i.changemode("aleatory.coin")
            _color.output_green(" The object 'aleat3.Aleatoryous' is OK.")
        except:
            _color.output_red("ERROR: Something's wrong at object 'aleat3.Aleatoryous' test.")

        try:
            print("-Testing object 'aleat3.InitError'...")
            class killme:
                def __init__(self):
                    raise InitError(f"Test info")
            _color.output_green(" The object 'aleat3.InitError' is OK.")
        except:
            _color.output_red("ERROR: Something's wrong at object 'aleat3.InitError' test.")

        print("Testing coin conversions...")
        time.sleep(0.7)
        print("-Testing 'coinToBinary'...")
        if coinToBinary(i.single()) in [1, 0]:
            _color.output_green(" The coin conversion 'coinToBinary' is OK.")
        else:
            _color.output_red("ERROR: Something's wrong at coin conversion 'coinToBinary'.")

        print("-Testing 'coinToBool'...")
        if coinToBool(i.single()) in [True, False]:
            _color.output_green(" The coin conversion 'coinToBool' is OK.")
        else:
            _color.output_red("ERROR: Something's wrong at coin conversion 'coinToBool'.")
        _color.output_green("The module is OK.")
    except:
        _color.output_red("ERROR: Something's wrong in the module.")

    _color.output_magenta("----Test finshed----")
    #print("----Test finished----\n")
    time.sleep(1)
    i = input("Done")


# ifmain function
if __name__ == '__main__':
    _color.output_yellow("NOTE: When using this file as __main__ level, you are executing the module test. This operation may take some minutes.")
    import time
    time.sleep(1.5)
    module_test()
