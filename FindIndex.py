list_of_elems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test', 'Ok']
elem = 'is'
pos = -1
# Iterate over list items by index pos
for i in range(len(list_of_elems)):
    # Check if items matches the given element
    if list_of_elems[i] == elem:
        pos = i
        break
if pos > -1:
    print(f'Index of element "{elem}" in the list is: ', pos)
else:
    print(f'Element "{elem}" does not exist in the list: ', pos)