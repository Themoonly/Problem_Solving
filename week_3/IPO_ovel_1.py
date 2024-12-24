
while True:
    i = int(input("Enter 1 : exit program or 2 : enter to program :"))

    if i == 2:
        hour = float(input("Enter hour : "))
        paylate = float(input("Enter paylate : "))

        if hour <= 160:
            total = hour * paylate
            print(f"paylate_b {total}")
        else:
            late_1 = (paylate * 160) + ((hour - 160) * (paylate * 1.5))

            print(f"paylate_a {late_1:.2f}")

        print("**Program is running**")
        continue
    
    else:
        print("**Program exit now**")
        break