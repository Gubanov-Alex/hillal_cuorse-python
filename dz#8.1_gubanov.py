def add_one(some_list):

    numb_srch = int("".join(str(el) for el in some_list)) + 1

    result =  []
    for el in str(numb_srch):
        result.append(int(el))
    return result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")