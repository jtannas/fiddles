#!/usr/bin/env python3
"""Normal implementation of fizzbuzz, nothing special"""

for num in range(1, 100 + 1):

    # Perform the logic tests so they are not repeated
    is_divisible_by_3 = (num % 3 == 0)
    is_divisible_by_5 = (num % 5 == 0)

    # Check all branches
    if is_divisible_by_3 and is_divisible_by_5:
        print('FizzBuzz')
    elif is_divisible_by_3:
        print('Fizz')
    elif is_divisible_by_5:
        print('Buzz')
    else:
        print(num)
