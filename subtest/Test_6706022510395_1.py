round_hous = []
while True:
    print(" --------------------------------------- ")
    print(" ประเภทของการออกกำลังกาย   การเผาผลาญต่อนาที")
    print(" --------------------------------------- ")
    print(" 1. Running (วิ่ง)          10 แคลอรี่ต่อนาที ")
    print(" 2. Cycling (ปั่นจักรยาน)    8 แคลอรี่ต่อนาที ")
    print(" 3. Swimming (ว่ายน้ำ)      5 แคลอรี่ต่อนาที ")
    print(" --------------------------------------- ")

    choices = int(input("Enter choices : "))
    hous = int(input("Enter hous : "))

    if choices == 1:
        total = hous * 60
        total_cal = total * 10
        round_hous.append([f"Time :{hous} cal :{hous*10}"])
        print(f"เวลาในการวิ่ง {total} นาที")
        print(f"สามารถเผาผลาญแคลอรี่ได้ {total_cal} แคลลอรี่")
    elif choices == 2:
        total = hous * 60
        total_cal = total * 8
        print(f"เวลาในการปั่นจักรยาน {total} นาที")
        print(f"สามารถเผาผลาญแคลอรี่ได้ {total_cal} แคลลอรี่")
    elif choices == 3:
        total = hous * 60
        total_cal = total * 5
        print(f"เวลาในการว่ายน้ำ {total} นาที")
        print(f"สามารถเผาผลาญแคลอรี่ได้ {total_cal} แคลลอรี่")
    else:
        error = str(input("ตัวเลือกที่คุณเลือกไม่มีใน choices คุณต้องการทำต่อหรือไม่ (y) to continue : "))
        if error == 'y':
            continue
        else:
            break

print(round_hous)