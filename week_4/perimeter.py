try:
    width = float(input("enter widthh : "))
    length = float(input("enter length : "))
    perimeter = (width + length) * 2
    print(f"perimeter = {perimeter:.2f} ")
except ValueError:
    print("plase enter number!!!")