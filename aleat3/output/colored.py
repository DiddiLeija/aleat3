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

error_text = """Unable to load Colorama. Some fuctions may not run correctly
without this package. You can download the package with pip:

            pip install colorama
"""

try:
    from colorama import Fore, Back, Style, init
    UNABLE = True
    init(autoreset=True)
    def output_red(message: str) -> None:
        print(Fore.RED + message)

    def output_yellow(message: str) -> None:
        print(Fore.YELLOW + message)

    def output_green(message: str) -> None:
        print(Fore.GREEN + message)

    def output_blue(message: str) -> None:
        print(Fore.BLUE + message)

    def output_magenta(message: str) -> None:
        print(Fore.MAGENTA + message)

    def output_bright(message: str) -> None:
        print(Style.BRIGHT + message)
except ImportError:
    print(error_text)
    UNABLE = False
    def base(a: str) -> None:
        print(a+"\n")
    # new: all the "patch functions" are just aliases
    # of "base()"...
    output_red = base
    output_green = base
    output_yellow = base
    output_blue = base
    output_magenta = base
    output_bright = base
    # doing this will let us to simplify all
    # the annotation/documentation works.
except Exception as e:
    import warnings
    warnings.warn("An unexpected error ocurred: '%s'. "%str(e)
                  "Some functions may fail without this colored functions. Report this "
                  "to <github.com/diddileija/diddiparser/issues/new>", 
                  UserWarning)


#########################################################################################################################################
"New since 0.1.1: Module test"

def module_test() -> None:
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
