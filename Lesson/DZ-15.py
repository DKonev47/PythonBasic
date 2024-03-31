number = int(input("Enter number: "))
day_x, hour_ost = divmod(number, 86400)
hour_x, minet_ost = divmod(hour_ost, 3600)
minet_x, second_x = divmod(minet_ost, 60)
day = ""
if day_x == 1 or (day_x > 20 and day_x % 10 == 1):
    day = ("День")
elif (day_x >= 2 and day_x <= 4) or (((day_x % 10 == 2) or (day_x % 10 == 3) or (day_x % 10 == 4)) and (day_x > 20)):
    day = ("Днi")
else:
    day = ("Днiв")
print(f'{day_x} {day}, {str(hour_x).zfill(2)}:{str(minet_x).zfill(2)}:{str(second_x).zfill(2)}')
