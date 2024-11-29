# หาผลรวมของตัวเลขในช่วงที่กำหนด
print("Calculate the sum between start and stop number")
x = int(input("Enter the start number: "))
y = int(input("Enter the end number: "))
listed = []

for a in range(x,y+1):
    listed.append(a)
print(f"The sum from {x} to {y} is: {sum(listed)}")
    

