"""Generic functions to return error messages."""
from typing import Any

def parameter_bug(arg: Any) -> str:
    return f"__init__() Invalid Syntax (Unexpected 'extras' given: {arg} when a list was expected)"

def KI_bug() -> str:
    return f"Program Interrupted by User..."

def modal_bug(arg: str) -> str:
    return f"__init__() Invalid Syntax (Unexpected 'mode' given: {arg} when a list was expected)"
