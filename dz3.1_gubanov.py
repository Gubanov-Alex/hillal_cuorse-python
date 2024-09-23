number1 = input("Enter a number '1': ")
number2 = input("Enter a number '2': ")
user_action = input("Enter an action (*,/,+,-): ")
if user_action == "*":
    result = float(int( number1 )*int(number2))
elif user_action == "+":
    result = float(int( number1 )+int(number2))
elif user_action == "-":
    result = float(int(number1) - int(number2))
elif user_action == "/":
    if number2  == "0":
        result = "Zero division prohibited.\nPut a correct data!"
    else:
        result = float(int(number1) / int(number2))
elif user_action != "*,/,+,-":
    result = "Types prohibited.\nPut a correct data for action!"

print(result)


