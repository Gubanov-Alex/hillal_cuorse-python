def common_elements():
    a_1 = []
    b_1 = []
    for i in range(100):
        if i % 3 == 0 :
            a_1.append(i)

    for a in range(100):
        if a % 5 == 0:
            b_1.append(a)

    a_set = set(a_1)
    b_set = set(b_1)
    result = a_set.intersection(b_set)
    return result



assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

