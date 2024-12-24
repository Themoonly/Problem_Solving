while True:
    
    numstart = int(input("Enter start_number : "))
    numend = int(input("Enter end_number : "))
    devide = int(input("Enter devide_number : "))

    for number in range(numstart+1,numend):
        if number % devide == 0:
            print(f"number = {number}")
    Press = int(input("Exit Press 0, continue Press 1 "))

    if Press == 0:
        print("Bye")
        break
    else:
        continue

    