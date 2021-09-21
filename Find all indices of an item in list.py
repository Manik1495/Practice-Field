
def get_indices_elem_inlist(list_of_elems, char):
    index_pos = 0
    index_list = []
    while True:
        try:
            index_pos = list_of_elems.index(char, index_pos)
            index_list.append(index_pos)
            index_pos += 1

        except ValueError as e:
            break
    
    return index_list

list_of_elems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test', 'Ok']


index_pos_list = get_indices_elem_inlist(list_of_elems, 'Ok')

print(index_pos_list)