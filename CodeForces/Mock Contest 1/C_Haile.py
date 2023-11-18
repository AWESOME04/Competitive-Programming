students = []
len_students = int(input())
for _ in range(len_students):
    curr_student = input()
    students.append(curr_student)

for value in students:
    print(value.replace('#', ' '))
   
