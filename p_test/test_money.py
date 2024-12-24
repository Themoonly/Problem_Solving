money = int(input("Enter money : "))
year = int(input("Enter year : "))
choice = int(input("enter choie 1 = day , 2 = month : "))

if choice == 1:
    money = money / (year * 365)
    print(f"ออมเงินรายวัน วันละ = {money}")
else:
    money = money / (year * 12)
    print(f"ออมเงินรายเดือน เดือนละ = {money}")