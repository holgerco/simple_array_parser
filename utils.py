from typing import List


def convert_to_ascii(number: int) -> str:
    """
    Function to convert digits of number to respective ASCII values
    Returns: ASCII values of number.

    """
    ascii_code = ''
    while number > 0:
        digit = number % 10
        ascii_code = F'{digit + 48}' + ascii_code
        number = number // 10
    return ascii_code


def ascii_to_digit(ascii_code: str) -> int:
    """
    Function to convert ASCII values to respective digits of number
    Args:
        ascii_code: ASCII code
    Returns: number
    """
    number = 0
    for index in range(0, len(ascii_code), 2):
        number *= 10
        character_ascii_code = ascii_code[index: index + 2]
        number += int(character_ascii_code) - 48
    return number


def array_to_number(arr: List[int]):
    """
    Args:
        arr: List of numbers to parse
    Returns: specific number
    """
    parsed_number = str()
    for number in arr:
        parsed_number = f'{parsed_number}{convert_to_ascii(number)}00'
    return parsed_number


def number_to_array(number: str) -> List[int]:
    """
    convert number to list of integers.
    """
    ascii_codes = number.strip('00').split('00')
    return [ascii_to_digit(ascii_code) for ascii_code in ascii_codes]
