#!/usr/bin/env python3
"""One logical line implementation of FizzBuzz

Source: http://michaeljgilliland.blogspot.ca/2013/01/one-line-fizz-buzz-test-in-python.html
"""

print('\n'.join("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i)
                for i in range(1, 101)))
