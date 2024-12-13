import time
print("***calculate sum of odd and even number (Exit press 0)***")

odded = []
evened = []

while True:
    number = int(input("Enter number : "))
    start = time.time()
    if number != 0:

        if number % 2 == 0:
            evened.append(number)
        else:
            odded.append(number)
            
    else:
        print(f"sum of even numbers = {sum(evened)}")
        print(f"sum of odd numbers = {sum(odded)}")
        print(f"time : {(time.time()-start)*1000}")
        break
