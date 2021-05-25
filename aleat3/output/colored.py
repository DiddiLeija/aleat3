"""
New since 0.0.9: Use console-colored functions.

This file uses Colorama (http://pypi.org/project/colorama) for colored output.
"""

__all__ = ["UNABLE",
           "output_red",
           "output_green",
           "output_yellow",
           "output_blue",
           "output_magenta",
           "output_bright"]

error_text = """Unable to load Colorama package. Some fuctions may not run correctly
without this function. You can download the package at the PyPi page:

            http://pypi.org/project/colorama
"""

try:
    from colorama import Fore, Back, Style, init
    __all__ = __all__ + ["Fore", "Back", "Style", "init"]
    UNABLE = True
    init(autoreset=True)
    def output_red(message):
        print(Fore.RED + message)

    def output_yellow(message):
        print(Fore.YELLOW + message)

    def output_green(message):
        print(Fore.GREEN + message)

    def output_blue(message):
        print(Fore.BLUE + message)

    def output_magenta(message):
        print(Fore.MAGENTA + message)

    def output_bright(message):
        print(Style.BRIGHT + message)
except ImportError:
    print(error_text)
    UNABLE = False
    def base(a):
        print(a+"\n")

    def output_red(message=None):
        base(message)

    def output_green(message=None):
        base(message)

    def output_yellow(message=None):
        base(message)

    def output_blue(message=None):
        base(message)

    def output_magenta(message=None):
        base(message)

    def output_bright(message=None):
        base(message)
except Exception as e:
           import warnings
           warnings.warn("An unexpected output ocurred: '%s'. "%str(e)
                         "Some functions may fail without that. Report this "
                         "to <github.com/diddileija/diddiparser/issues>", UserWarning)


#########################################################################################################################################
"New since 0.1.1: Module test"

def module_test():
    output_magenta("----Module Test: colored.py----")
    print("Available colors demostration:")
    output_red(" -Red output")
    output_green(" -Green output")
    output_yellow(" -Yellow output")
    output_blue(" -Blue output")
    output_magenta(" -Magenta output")
    print("Some style demostration")
    output_bright(" -Bright output")
    print("\n" + "Colorama package:", UNABLE)
    if not UNABLE:
        print(error_text)
    print()
    output_green("The module is OK.")
    output_magenta("----Test finished----")
    d = input("\n" + "Done")

if __name__ == '__main__':
    output_yellow("NOTE: When using this file as __main__ level, you are executing the module test. This operation may take some minutes.")
    module_test()
