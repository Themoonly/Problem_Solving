numstart = int(input("Enter start_number : "))
numend = int(input("Enter end_number : "))
# list = []
for number in range(numstart+1,numend):
    if number % 3 == 0:
        print(f"number = {number}")
        # list.append(number)
        # print(f"complace!!! {list}")