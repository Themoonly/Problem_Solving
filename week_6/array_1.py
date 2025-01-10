import array as arr

number = arr.array('i', [50, 87, 65, 39])
for i in number:
    print(i, end=" ")
print()


num_max = max(number)
num_min = min(number)
num_sum = sum(number)
num_averages = num_sum / len(number)
sort_min_to_max = sorted(number)
sort_max_to_min = (sorted(number))[::-1] # แก้

print(f"Max = {num_max}, Min = {num_min}")
print(f"Sum = {num_sum}, Averages = {num_averages}")
print(f"min to max = {sort_min_to_max}")
print(f"max to min = {sort_max_to_min}")

for i in number:
    if i % 2 == 0:
        print(f"even number = {i}")
    else:
        print(i)


