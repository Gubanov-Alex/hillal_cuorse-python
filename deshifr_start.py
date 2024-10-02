alfavit_shifr = ("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ")

cod_step = int(input('Step for code:'))
cod_text = input('Text for code:').upper()
result1 = ''
result2 = ''

cod_shifr = int((cod_step*3)/2+7)
cod_shifr2 = int((cod_step*9)/3+3)
print(cod_shifr, cod_shifr2)

for letter in cod_text:
    place = alfavit_shifr.find(letter)
    cod_place = place - cod_shifr2
    if letter in alfavit_shifr:
        result1 += alfavit_shifr[cod_place]
    else:
        result1 += letter

for letter in result1:
    place = alfavit_shifr.find(letter)
    cod_place = place - cod_shifr
    if letter in alfavit_shifr:
        result2 += alfavit_shifr[cod_place]
    else:
        result2 += letter

print(result2)