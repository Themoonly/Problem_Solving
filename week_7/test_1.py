student_list = []
number_of_student = int(input("Enter the number of students: "))

for i in range(number_of_student):
    name_std = input(f"Enter student name {i + 1}: ")
    score_std = float(input(f"Enter student score {i + 1}: "))
    student_list.append([name_std, score_std])  # เก็บข้อมูลเป็น list [ชื่อ, คะแนน]

print("\n-- Unsorted Score --")
for student in student_list:
    print(f"{student[0]} : {student[1]}")

# ใช้ Selection Sort เพื่อเรียงลำดับคะแนนจากมากไปน้อย
for i in range(len(student_list)):
    max_index = i
    for j in range(i + 1, len(student_list)):
        if student_list[j][1] > student_list[max_index][1]:  # เปรียบเทียบคะแนน
            max_index = j
    # สลับตำแหน่ง
    temp = student_list[i]
    student_list[i] = student_list[max_index]
    student_list[max_index] = temp

print("\n-- Sorted Score (Descending Order) --")
for student in student_list:
    print(f"{student[0]} : {student[1]}")
