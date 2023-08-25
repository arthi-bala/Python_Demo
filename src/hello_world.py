"""
This module is used for printing the senetnce given by user.

Input:
>>> This is sample text
Output:
>>> Hello, This is sample text
"""

import pytest

def print_statement(input_str: str) -> str:
    """To print the text given by the user along with hello.

    Args:
        input_str (str): The input text to br printed

    Returns:
        str: The text to be printed along with hello
    """
    result = "Hello"
    return "Hello, " + input_str + result


if __name__ == "__main__":
    RESULT = print_statement("This is sample text")

    for letter in RESULT:
        print(letter)
    if RESULT is None:
        print("Hi")
    pytest.main()
