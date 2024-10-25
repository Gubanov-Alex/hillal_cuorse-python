def difference_between_numbers (*args:int or float)->int or float:
    """
    Checking difference between min & max numbers.

    :param *args: numbers for checking.
    :type *args: int or float.
    :return: result of difference between min & max.
    :rtype: int or float.
    """
    #1 - Simple:
    if not args:
        return 0
    return round(max(args) - min(args), 2)

    #2 - Little more difficult
    # if not args:
    #     return 0
    #
    # def recurs_find_minmax(index, current_min, current_max):
    #     """"
    #     Recursive function
    #     selecting from all min & max values, the ending condition is the number of elements (args).
    #     """
    #     if index == len(args):                       #recurs break condition
    #         return current_min, current_max
    #     new_min = min(current_min, args[index])      # recurs element
    #     new_max = max(current_max, args[index])      # recurs element
    #     return recurs_find_minmax(index + 1, new_min, new_max) # recurs iteration
    #
    # final_min, final_max = recurs_find_minmax(0, args[0], args[0]) # Final condition
    #
    # return round(final_max - final_min, 2)

assert difference_between_numbers (1, 2, 3) == 2, 'Test1'
assert difference_between_numbers (5, -5) == 10, 'Test2'
assert difference_between_numbers (10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference_between_numbers () == 0, 'Test4'
print('OK')