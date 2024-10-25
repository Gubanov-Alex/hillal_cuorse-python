def is_even(number:int)->bool:
    """
    Found number is even or not using a bitwise operation.

    :param number: numbers for checking.
    :type number: int.
    :return: result of checking.
    :rtype: bool.
    """

    return (number & 1) == 0   # using a bitwise 'AND' operation.

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print("You're good,yeeaa!")