#!/usr/bin/python3
roman_digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                'M': 1000, '0': 0}


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_string += '0'
    i, sum = 0, 0
    while i < len(roman_string) - 1:
        this = roman_digits[roman_string[i]]
        next = roman_digits[roman_string[i + 1]]
        if this == next:
            sum += next + this
            i += 1
        elif this < next:
            sum += next - this
            i += 1
        else:
            sum += this
        i += 1
    return sum
