active = True
while active:
    user_choice = input("What action Bro?-choose 'Yes' or 'NO':").lower()
    if user_choice == 'yes' or user_choice == 'ye' or user_choice == 'y' :
        number1 = input("Enter a number '1': ")
        number2 = input("Enter a number '2': ")
        user_action = input("Enter an action (*,/,+,-): ")
        if user_action == "*":
            result = float(float(number1) * float(number2))
        elif user_action == "+":
            result = float(float(number1) + float(number2))
        elif user_action == "-":
            result = float(float(number1) - float(number2))
        elif user_action == "/":
            if number2 != "0":
                result = float(float(number1) / float(number2))
            else:
                result = "Zero division prohibited.\nPut a correct data!"
        elif user_action != "*,/,+,-":
            result = "Types prohibited.\nPut a correct data for action!"
        print(result)

    elif user_choice == "no" or user_choice == 'n' :
        active = False
        print("Ostalavista Baby!")

    else:
        print("I'm just a calculator-Whatss'up@@?")
