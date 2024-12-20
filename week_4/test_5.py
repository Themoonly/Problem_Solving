sum = 0
for i in range(1,12):
    age = int(input(f"{i} Enter Age : "))
    sum = sum + age
average = sum / (i)
print(f"average {average}")