
def format_name(f_name,l_name):
    # f_name = str.lower(f_name)
    # l_name = str.lower(l_name)
    f_name = str.title(f_name)
    l_name = str.title(l_name)
    result = f_name + " " +l_name
    return result




first_name = input("Your firstname: \n")
last_name = input("Your lastname: \n")
output = format_name(first_name,last_name)
print(output)