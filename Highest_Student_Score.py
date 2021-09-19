# list_of_scores = input("Enter the scores here : ")
# list_of_scores = list(list_of_scores.split(" "))
# print(list_of_scores)

# highest = 0
# for score in list_of_scores:
#     if highest < int(score):
#         highest = int(score)

# print(highest)

# split() converts str to list.

list_of_scores = input("Enter the scores here : ")
list_of_scores = list_of_scores.split(" ")
# print(type(list_of_scores))
len_list = len(list_of_scores)


#script to convert list of strings to list of int.
n = 0
int_list_of_scores = []
for i in list_of_scores:
    int_list = int(i)
    # print(int_list)
    # print(n)
    if n < len_list:
        int_list_of_scores.append(int_list)
print(int_list_of_scores)

highest = 0
for score in int_list_of_scores:
    if highest < score:
        highest = score

print(highest)





