import math
def prime_generator(end:int)->list:
    """
        Generator function prime_generator, which is a generator of prime numbers.
        The upper limit of this range is
        determined by the parameter of this function.
        :param end: Number of the end of the range.
        :type end: int.
        :return: List of prime numbers.
        :rtype: list.
        """
    if end < 2:           # End function for value < 2 (opt. level)
        return
    yield 2
    for x in range(3, end + 1, 2):         # Check for just odd numbers
        if all(x % y != 0 for y in range(3, int(math.sqrt(x)) + 1, 2)):  # Use sqrt, for optimize since the divisor
            yield x                                              #  of a number cannot be greater than it's square root.


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(1)) == [], 'Test1.1'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')