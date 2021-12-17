#!/usr/bin/python3
"""Module to print a text"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after '.','?',':'
    Arg: text - to be printed
    Raises: TypeError - if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
