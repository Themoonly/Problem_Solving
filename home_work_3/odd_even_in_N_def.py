import time

def num_odd_even(number):
    num_odd = 0
    num_even = 0
    for num in range(1,number + 1):
        if num % 2 == 0:
            num_even += num
        else:
            num_odd += num
    return num_even,num_odd
    
number = int(input("enter number : "))

start_time = time.time()

num_odd, num_even = num_odd_even(number)

stop_time = time.time()

print(f"sum of odd number = {num_odd}")
print(f"sum of odd number = {num_even}")
print(f"number = {number}, time = {stop_time - start_time:.6f}, Big O = ??")
