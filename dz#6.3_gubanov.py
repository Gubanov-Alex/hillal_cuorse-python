from functools import reduce
from operator import mul

user_number = int(input("Input  number:"))

a_sp = []

while user_number > 9:
    user_number = str(user_number)
    a_sp.clear()
    for letra in user_number:
        b_sp = int(letra)
        a_sp.append(b_sp)
        user_number = reduce(mul, a_sp)

print(user_number)