spisok_1 = [12,3,4,10,] #     leave an "if" checking,because we are working with a list,not a tuple.
if len(spisok_1) <= 1:
    print(spisok_1)
else:
    transfer_number = spisok_1.pop(-1)
    spisok_1.insert(0,transfer_number)
    print(spisok_1)

spisok_1 = [1]
if len(spisok_1) <= 1: # leave "if" checking,because we are working with a list,not a tuple.
    print(spisok_1)
elif len (spisok_1) > 1:
    transfer_number = spisok_1.pop(-1)
    spisok_1.insert(0,transfer_number)
    print(spisok_1)

spisok_1 = []
if len(spisok_1) <= 1: # leave "if" checking,because we are working with a list,not a tuple.
    print(spisok_1)
elif len (spisok_1) > 1:
    transfer_number = spisok_1.pop(-1)
    spisok_1.insert(0,transfer_number)
    print(spisok_1)

spisok_1 = [12, 3, 4, 10, 8 ]
if len(spisok_1) <= 1: # leave "if" checking,because we are working with a list,not a tuple.
     print(spisok_1)
else:
    transfer_number = spisok_1.pop(-1)
    spisok_1.insert(0,transfer_number)
    print(spisok_1)