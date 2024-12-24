# 1. input number ตัวแปร
# 2. loop sum in range number
# 3. check number and sum number odd or even
# 4. import time

# รับโมดูลเวลา
import time

# input parameter
number = int(input("Enter number : "))
num_odd = 0
num_even = 0

# start time
start_time = time.time()

# for sum even and odd
for num in range(1, number + 1):
    if num % 2 == 0:
        num_even += num
    else:
        num_odd += num

# stop time
end_time = time.time()

# print
print(num_odd)
print(num_even)
print(f"{end_time - start_time:.6f}")


