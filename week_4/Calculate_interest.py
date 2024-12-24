amount = float(input("Enter amount : "))
if amount >= 1 and amount <= 1000:
    print("ดอกเบี้ยร้อยละ 10 ")
    print(f"amount + ดอกเบี้ย = {amount + ((amount * 10) / 100)}")
elif amount >= 1001 and amount < 10000:
    print("ดอกเบี้ยร้อยละ 5 ")
    print(f"amount + ดอกเบี้ย = {amount + ((amount * 5) / 100)}")
else:
    print("ดอกเบี้ยร้อยละ 2 ")
    print(f"amount + ดอกเบี้ย = {amount + ((amount * 2) / 100)}")
