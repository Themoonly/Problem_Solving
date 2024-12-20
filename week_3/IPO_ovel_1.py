
while True:
    i = int(input("Enter 1 : break or 2 : continue :"))
    if i == 2:
        hour = float(input("Enter hour : "))
        paylate = float(input("Enter paylate : "))

        if hour <= 160:
            total = hour * paylate
            print(f"paylate_b {total}")
        else:
            late_1 = (160 - paylate) * ((hour - 160) * (paylate * 1.5))

            print(f"paylate_a {late_1:.2f}")

        print("**Program is continue**")
        continue
    
    else:
        print("**Program break now**")
        break