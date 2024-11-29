# คำนวณดัชนีมวลกาย สูตร BMI

print("***Convert BMI***")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m) : "))

BMI = weight/(height**2)

print(f"Your BMI is: {BMI:.5f}")