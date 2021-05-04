"""At this place, we give only the messages for raising."""

def parameter_bug(arg):
    return f"__init__() Invalid Syntax (Unexpected 'extras' given: {arg} when a list was expected)"

def KI_bug():
    return f"Program Interrupted by User..."

def modal_bug(arg):
    return f"__init__() Invalid Syntax (Unexpected 'mode' given: {arg} when a list was expected)"

######################################################################################################################################################
def module_test(main_level=False):
    tmp = [f"__init__() Invalid Syntax (Unexpected parameter given: mode)",
           f"Program Interrupted by User...",
           f"__init__() Invalid Syntax (Unexpected parameter given: extras)"]
    if main_level:
        from colored import output_red, output_green, output_magenta
    else:
        from aleat3.output.colored import output_red, output_green, output_magenta
    output_magenta("----Module test: init_errors.py----")
    print("Testing functions...\n")
    if parameter_bug() == tmp[2]:
        output_green("-parameter_bug OK")
        if KI_bug() == tmp[1]:
            output_green("-ki_bug OK")
            if modal_bug() == tmp[0]:
                output_green("-modal_bug OK")
                output_green("The module is OK.")
    else:
        output_red("ERROR: Something failed at test.")
    output_magenta("----Test finished----")
    i = input("Done")

if __name__ == '__main__':
    from colored import output_yellow
    output_yellow("NOTE: When using this file as __main__ level, you are executing the module test. This operation may take some minutes.")
    module_test(True)
