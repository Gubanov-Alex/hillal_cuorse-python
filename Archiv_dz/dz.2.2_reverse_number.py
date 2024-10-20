user_number = input("Enter a number: ")
number_5= int(int(user_number) // 1) % 10
number_4= int (int(user_number) //10)  % 10
number_3= int (int (user_number)  // 100 ) % 10
number_2= int (int (user_number)  // 1000 ) % 10
number_1= int (int(user_number)) // 10000

back_number = (f'{number_5}{number_4}{number_3}{number_2}{number_1}')
print(back_number)

