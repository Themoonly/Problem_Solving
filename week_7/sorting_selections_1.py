list_student = []
number_of_students = int(input("Enter the number of students : "))

for round_std in range(number_of_students):
    name_std = input(f"Enter student name {round_std + 1} : ")
    score_std = float(input(f"Enter student score {round_std + 1} : "))
    list_student.append([name_std, score_std])

print("\n--unsort score--")
for unsort_score in list_student:
    print(f"name {unsort_score[0]} : score {unsort_score[1]}")

for sort_score in range(len(list_student)):
    position_max = sort_score
    for pos_score in range(sort_score + 1,(len(list_student))):
        if list_student[pos_score][1] > list_student[position_max][1]:
            position_max = pos_score

            temp = list_student[sort_score]
            list_student[sort_score] = list_student[position_max]
            list_student[position_max] = temp

print("\n--sort score(selections)--")
for sorted_score in list_student:
    print(f"name {sorted_score[0]} : score {sorted_score[1]}")

print("\n--top 3 hightest score--")
top_student = list_student[:3]
round = 1
for student in top_student:
    print(f" Top {round} : {student[0]} : {student[1]} ")
    round += 1

print("\n--top 3 lowest score--")

for sort_score in range(len(list_student)):
    position_max = sort_score
    for pos_score in range(sort_score + 1,(len(list_student))):
        if list_student[pos_score][1] < list_student[position_max][1]:
            position_max = pos_score

            temp = list_student[sort_score]
            list_student[sort_score] = list_student[position_max]
            list_student[position_max] = temp

top_student = list_student[-3:]
round = len(list_student) - 2
for student in top_student:
    print(f" Top {round} : {student[0]} : {student[1]} ")
    round += 1

search_score = float(input("\nEnter student score to search: "))  
found = False

for student in list_student:
    if student[1] == search_score:  
        print(f"Found: {student[0]} - Score: {student[1]}")
        found = True

if not found:
    print(f"Student with this score not found. {search_score}")