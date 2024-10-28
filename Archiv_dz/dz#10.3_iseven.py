def is_even(digit:int)->bool:
        """
        Found number is even or not.

        :param digit: numbers for checking.
        :type digit: int.
        :return: result of checking.
        :rtype: bool.
        """


        return digit % 2 == 0

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')