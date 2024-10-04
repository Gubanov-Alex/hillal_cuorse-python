from functools import reduce
from operator import mul

user_number = input("Input  number:")

a_sp = []                                  #Making a list for counting
for letra in user_number:                  #Changing type for function
        b_sp= int(letra)
        a_sp.append(b_sp)
result = reduce(mul, a_sp)                 #Function for result

while result > 9:
    result = str(result)
    a_sp.clear()
    for letra in result:
        b_sp = int(letra)
        a_sp.append(b_sp)
        result = reduce(mul, a_sp)

print(result)