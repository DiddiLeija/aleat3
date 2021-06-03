"""Generic functions to return error messages."""

def parameter_bug(arg):
    return f"__init__() Invalid Syntax (Unexpected 'extras' given: {arg} when a list was expected)"

def KI_bug():
    return f"Program Interrupted by User..."

def modal_bug(arg):
    return f"__init__() Invalid Syntax (Unexpected 'mode' given: {arg} when a list was expected)"
