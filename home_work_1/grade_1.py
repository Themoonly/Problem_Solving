number_of_students = int(input("first Enter number of students : "))
print(f"number_of_students = {number_of_students}")
for numstudents in range(number_of_students):
    grades = int(input(f"enter grade of students {numstudents+1} : "))
    if grades >= 80:
        print(f"you grade = A")
    elif grades >= 75:
        print(f"you grade = B+")
    elif grades >= 70:
        print(f"you grade = B")
    elif grades >= 65:
        print(f"you grade = C+")
    elif grades >= 60:
        print(f"you grade = C")
    elif grades >= 55:
        print(f"you grade = D+")
    elif grades >= 50:
        print(f"you grade = D")
    else:
        print(f"you grade = F")
