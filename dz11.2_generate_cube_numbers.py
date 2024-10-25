def generate_cube_numbers(end:int)->list:
    """
         Generator function cube_numbers_generator, which is a generator of cube's numbers.
         The upper limit of value this range is
         determined by the parameter of this function.
         :param end: Number value of the end of the range.
         :type end: int.
         :return: List of cube's numbers.
         :rtype: list.
         """
    # if end < 8:
    #     return                                 # Checking start the generator for values less than 8.
    # for x in range(2,end):
    #          cube = x ** 3
    #          if cube <= end:
    #             yield cube
    #          else:
    #             return

    if end < 8:                            # Checking  start the generator for values less than 8.
        return
    x = 2
    while True:
        cube = x ** 3
        if cube <= end:
           yield cube
        else:
            return
        x += 1




from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(1)) == []
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print("You're good,yeeaa!")