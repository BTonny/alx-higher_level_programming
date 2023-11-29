#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    L = len(text)
    i = 0
    while i < L and text[i] == " ":
        i += 1
    while i < L:
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < L and text[i] == ' ':
                i += 1
            continue
        i += 1