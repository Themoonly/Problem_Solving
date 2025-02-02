def get_student_data():
    """รับข้อมูลนักเรียนจากผู้ใช้"""
    list_student = []
    number_of_students = int(input("Enter the number of students: "))
    
    for round_std in range(number_of_students):
        name_std = input(f"Enter student name {round_std + 1}: ")
        score_std = float(input(f"Enter student score {round_std + 1}: "))
        list_student.append([name_std, score_std])
    
    return list_student

def display_students(title, students):
    """แสดงข้อมูลนักเรียน"""
    print(f"\n-- {title} --")
    for student in students:
        print(f"Name: {student[0]} | Score: {student[1]}")

def selection_sort(students, descending=True):
    """เรียงลำดับคะแนนของนักเรียน (มากไปน้อยหรือน้อยไปมาก)"""
    for i in range(len(students)):
        pos = i
        for j in range(i + 1, len(students)):
            if (descending and students[j][1] > students[pos][1]) or (not descending and students[j][1] < students[pos][1]):
                pos = j
        students[i], students[pos] = students[pos], students[i]
    
    return students

def display_top_students(students, top_n=3, highest=True):
    """แสดงนักเรียนที่มีคะแนนสูงสุดหรือต่ำสุด"""
    title = "Top 3 Highest Scores" if highest else "Top 3 Lowest Scores"
    selected_students = students[:top_n] if highest else students[-top_n:]
    
    print(f"\n-- {title} --")
    for idx, student in enumerate(selected_students, start=1 if highest else len(students) - 2):
        print(f"Top {idx}: {student[0]} | Score: {student[1]}")

def search_student_by_score(students):
    """ค้นหานักเรียนโดยใช้คะแนน"""
    search_score = float(input("\nEnter student score to search: "))
    found = False
    
    for student in students:
        if student[1] == search_score:
            print(f"Found: {student[0]} | Score: {student[1]}")
            found = True
    
    if not found:
        print("Student with this score not found.")

def main():
    students = get_student_data()
    display_students("Unsorted Scores", students)
    
    sorted_students = selection_sort(students.copy(), descending=True)
    display_students("Sorted Scores (High to Low)", sorted_students)
    
    display_top_students(sorted_students, top_n=3, highest=True)
    
    sorted_students = selection_sort(students.copy(), descending=False)
    display_top_students(sorted_students, top_n=3, highest=False)
    
    search_student_by_score(students)

if __name__ == "__main__":
    main()