number1 = input("Enter a number '1': ")
number2 = input("Enter a number '2': ")
user_action = input("Enter an action (*,/,+,-): ")
if user_action == "*":
    result = float(float( number1 )*float(number2))
elif user_action == "+":
    result = float(float( number1 )+float(number2))
elif user_action == "-":
    result = float(float(number1) - float(number2))
elif user_action == "/":
    if number2  == "0":
        result = "Zero division prohibited.\nPut a correct data!"
    else:
        result = float(float(number1) / float(number2))
elif user_action != "*,/,+,-":
    result = "Types prohibited.\nPut a correct data for action!"

print(result)


