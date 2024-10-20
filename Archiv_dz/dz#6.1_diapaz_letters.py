import string

user_leter = input("input  letters (a-Z)*ex:")

range_look = string.ascii_letters
result = range_look [range_look.find(user_leter[0]):range_look.find(user_leter[2])+1]

print(result)

