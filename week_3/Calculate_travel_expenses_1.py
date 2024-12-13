while True:
    try:
        kilo = int(input("Enter kilomate : "))
        car = int(input("1 = รถน้ำมัน, 2 = รถไฟฟ้า :"))

        if car == 1:
            travel = kilo * 4
            print(f"ผลคำนวณค่าใช้จ่าย รถน้ำมัน {travel} บาทต่อกิโลเมตร")

        elif car == 2:
            travel = kilo * 1
            print(f"ผลคำนวณค่าใช้จ่าย รถไฟฟ้า {travel} บาทต่อกิโลเมตร")
        else:
            print("Plase enter car 1 or 2")
        break
    except:
        print("Plase enter number only!!!")
        continue