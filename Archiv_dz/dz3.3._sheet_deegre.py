spysok_all = [1, 2, 3, 4, 5, 6]
if len(spysok_all) %2 == 0:
    half_spisok1 = spysok_all[:len(spysok_all) // 2]
    half_spisok2 = spysok_all[len(spysok_all) // 2:]
else:
    half_spisok1 = spysok_all[:(len(spysok_all) // 2)+1]
    half_spisok2 = spysok_all[(len(spysok_all) // 2)+1:]

new_spisok = ([half_spisok1]+[half_spisok2])

print(new_spisok)
#############################################################
spysok_all = [1, 2, 3]                             #2 "If" checking condition for odd and shifts the list step if
                                                       # necessary.
if len(spysok_all) %2 == 0:
    half_spisok1 = spysok_all[:len(spysok_all) // 2]
    half_spisok2 = spysok_all[len(spysok_all) // 2:]
else:
    half_spisok1 = spysok_all[:(len(spysok_all) // 2)+1]
    half_spisok2 = spysok_all[(len(spysok_all) // 2)+1:]

new_spisok = ([half_spisok1]+[half_spisok2])

print(new_spisok)
########################################################3
spysok_all = [1, 2, 3, 4, 5]                            #3

if len(spysok_all) %2 == 0:
    half_spisok1 = spysok_all[:len(spysok_all) // 2]
    half_spisok2 = spysok_all[len(spysok_all) // 2:]
else:
    half_spisok1 = spysok_all[:(len(spysok_all) // 2)+1]
    half_spisok2 = spysok_all[(len(spysok_all) // 2)+1:]

new_spisok = ([half_spisok1]+[half_spisok2])

print(new_spisok)
##################################################################

spysok_all = [1]                                        #4

if len(spysok_all) %2 == 0:
    half_spisok1 = spysok_all[:len(spysok_all) // 2]
    half_spisok2 = spysok_all[len(spysok_all) // 2:]
else:
    half_spisok1 = spysok_all[:(len(spysok_all) // 2)+1]
    half_spisok2 = spysok_all[(len(spysok_all) // 2)+1:]

new_spisok = ([half_spisok1]+[half_spisok2])

print(new_spisok)

##############################################################################
spysok_all = []                                          #5

if len(spysok_all) %2 == 0:
    half_spisok1 = spysok_all[:len(spysok_all) // 2]
    half_spisok2 = spysok_all[len(spysok_all) // 2:]
else:
    half_spisok1 = spysok_all[:(len(spysok_all) // 2)+1]
    half_spisok2 = spysok_all[(len(spysok_all) // 2)+1:]

new_spisok = ([half_spisok1]+[half_spisok2])

print(new_spisok)

