user_time = int(input("Input  time in second (0-8640000):"))

day_user = divmod(user_time,86400)
hour_user = divmod(day_user[1],3600)
minute_user = divmod(hour_user[1],60)
second_user = minute_user[1]

day_end = "днів"
if  5 > day_user[0] > 1:
    day_end = "дні"
elif  day_user[0] % 10 == 1 and day_user[0] != 11:
    day_end = "день"

hour_res = str(hour_user[0])
minute_res = str(minute_user[0])
second_res = str(second_user)
if hour_user[0] < 10:
    hour_res = str(hour_user[0]).zfill(2)
if minute_user[0] < 10:
    minute_res = str(minute_user[0]).zfill(2)
if second_user < 10:
    second_res = str(second_user).zfill(2)

print(f"{day_user[0]} {day_end}, {hour_res}:{minute_res}:{second_res}")