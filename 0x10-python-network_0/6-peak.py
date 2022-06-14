#!/usr/bin/python3
"""Defines a function that finds the peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds the peak in a list of unsorted integers
    Args:
        list_of_integers (list): Unsorted list of integers to find peak of.
    Returns:
        int: The peak of the unsorted list.
    """
    length = len(list_of_integers)

    if length == 0:
        return None
    elif length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    list_of_integers.sort(reverse=True)

    return list_of_integers[0]
