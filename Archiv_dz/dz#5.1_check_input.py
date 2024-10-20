import keyword

user_input = input("Enter a variable: ")

if  user_input  in keyword.kwlist or user_input.count("_") > 1 :
    user_input = False
    print(user_input)
else :
    print(user_input.isidentifier())