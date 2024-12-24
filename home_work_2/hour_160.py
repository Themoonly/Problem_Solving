employee = int(input("Enter number of employee : "))

for num in range(employee):
    hour = int(input(f"Enter hour {num+1} : "))
    rate = int(input(f"enter rate {num+1} : "))
    if hour <= 160:
        print(f"Labor cost {hour * rate}")
    else:
        print(f"Labor cost {(rate * 160) + ((hour - 160) * rate * 1.5)}")