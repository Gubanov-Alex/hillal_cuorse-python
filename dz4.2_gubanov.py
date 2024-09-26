spisok_numbers = [1, 3, 5]
# spisok_numbers = [6]
# spisok_numbers = [0]

suma_spisok = sum(spisok_numbers[::2])
multi_numbers = suma_spisok * spisok_numbers[-1]

print(multi_numbers)