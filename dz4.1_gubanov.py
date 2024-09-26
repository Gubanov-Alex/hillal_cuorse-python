# spisok_numbers = [0, 1, 0, 12, 3]
# spisok_numbers = [0]
# spisok_numbers = [1, 0, 13, 0, 0, 0, 5]
spisok_numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for number in spisok_numbers:
    if number  == 0 :
        spisok_numbers.remove(number)
        spisok_numbers.append(number)

print(spisok_numbers)
