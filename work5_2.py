
# input ค่า
list_students = []
num_of_students = int(input("Enter the number of student : "))
for round_students in range(num_of_students):
    student_name = input(f"Enter student name {round_students+1} : ")
    student_score = float(input(f"Enter student score {round_students+1} : "))
    list_students.append(f"{student_name} : {student_score}")

# Print Unsorted
print("--Unsorted Score--")
for i in range(num_of_students):
    print(list_students[i])

# print Sorted
# list_students_2 = bubbleSort(list_students)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        print(passnum)
        for i in range(passnum):
            if alist[i][1]>alist[i][1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                
bubbleSort(list_students)
print("--Sorted score (selections)--")
for name,score in list_students:
    # print(f"{student_name[i][0]} : {student_score[i][1]}")
    print(f"{name} : {score}")