def get_students_data():
    list_students = []
    num_of_students = int(input("Enter the number of student : "))
    
    for found in range(num_of_students):
        name_std = input(f"Enter students name {found + 1} : ")
        score_std = float(f"Enter student score {found + 1} : ")
        list_students.append([name_std, score_std])

    return list_students

def print_students(student_data):
    print("\n--unsorted score--")
    for students_unsort in student_data:
        print(f"name {students_unsort[0]} : score {students_unsort[1]}")
    
def sorter_selections(list_students):
    for sort_score in range(len(list_students)):
        positions_max = sort_score
        for positions_score in range(sort_score + 1,(len(list_students))):
            if list_students[positions_score][1] < list_students[positions_max][1]:
                positions_max = positions_score

                temp = list_students[positions_score]
                list_students[positions_score] = list_students[positions_max]
                list_students[positions_max] = temp
    return temp

def find_top_3_highest(list_students):
    top_student = list_students[:3]
    round = 1
    for students in top_student:
        print(f"top {round} : {students[0]} : {students[1]}")
        round += 1

    return students

def find_top_3_lowest(list_students):
    top_students = list_students[-3:]
    round = len()

