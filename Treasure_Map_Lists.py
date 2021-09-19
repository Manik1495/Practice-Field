row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
# print(map)
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

a = list(str(position))
print(a)

col = a[0]
row = a[1]
int_row = int(row)
int_col = int(col)
print(col,row)
# if(col == 1 and row ==2):
#     print(row1.append("X"))

#     col--Index
#     row--which map

# (lst3[0][1]) -->listname[list_num][index]
#column, row

# list.insert(i, x)
# Insert an item at a given position. 
# The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

#map[0].insert(0,(1))
map[int_row-1][int_col-1]= "X"
#map[0][1] = "X"
# print(map)

print(f"{row1}\n{row2}\n{row3}")

