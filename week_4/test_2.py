width = float(input("enter widthh : "))
length = float(input("enter length : "))
if width or length >= 0:
    if width >= 0:
        width = float(input("enter widthh2 : "))
    else:
        length = float(input("enter length2 : "))

    perimeter = (width + length) * 2
print(f"perimeter = {perimeter:.2f} ")
