print("1 = +")
print("2 = -")
print("3 = *")
print("4 = /")

condition = int(input("Enter condition : "))
print(f"condition = {condition}")

number1 = int(input("Enter number1 : "))
number2 = int(input("Enter number2 : "))

if condition == 1:
    print(f"sum = {number1 + number2}")

elif condition == 2:
    print(f"sum = {number1 - number2}")

elif condition == 3:
    print(f"sum = {number1 * number2}")

elif condition == 4:
    print(f"sum = {number1 / number2}")



