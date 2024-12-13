import time
def Seq(num):
    total = 0
    for i in range(num):
        total += (i+1)
    return total

number = int(input("Enter number : "))
start = time.time()
print(f"ans {Seq(number)}")
print(f"time = {(time.time()-start)*1000}")