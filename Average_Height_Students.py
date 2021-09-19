student_ht = input("Enter the heights of students separated by space: \n")
#print(student_ht)
student_ht = list(student_ht.split(" "))
# list_of_st =  list(student_ht)
# print(list_of_st)
# print(student_ht)
sum_of_hts = 0
for student in student_ht:
    # print(s)
    sum_of_hts += int(student)

Average = round(sum_of_hts / len(student_ht))

print(f"Average height of class is :{Average}")


