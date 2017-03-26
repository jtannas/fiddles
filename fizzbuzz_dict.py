#!/usr/bin/env python3
"""Implementation of FizzBuzz using a dict to store the numbers/words.

Notes:
    - Turns FizzBuzz into a FizzBuzzer function for reuse.
    - Allows addition of addtional number/word pairs very easily.
    - Very pythonic; Does not translate readily to other languages.
    - Could be made more compact, but that'd be less readable
    - Nothing is printed until everything is ready.
"""


def FizzBuzzer(word_dict: dict, num: int):
    """Return word(s) if num is divisible by the word key(s), else num

    word_dict must be composed of numerical keys and string values"""

    print_buffer = ''

    for key, value in sorted(word_dict.items()):
        if num % key == 0:
            print_buffer += value

    return str(num) if print_buffer == '' else print_buffer


FIZZBUZZ_KEYS = {3: 'Fizz', 5: 'Buzz'}
NUMBERS = range(1, 100 + 1)

word_list = [FizzBuzzer(word_dict=FIZZBUZZ_KEYS, num=i) for i in NUMBERS]
print(*word_list, sep='\n')
