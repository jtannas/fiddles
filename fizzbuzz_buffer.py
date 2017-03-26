#!/usr/bin/env python3
"""Implementation of fizzbuzz by building a string"""

for num in range(1, 100 + 1):

    string_buffer = ''

    if num % 3 == 0:
        string_buffer += 'Fizz'

    if num % 5 == 0:
        string_buffer += 'Buzz'

    print(num if string_buffer == '' else string_buffer)
