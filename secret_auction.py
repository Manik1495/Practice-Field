from clear_console import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

is_user = True

bid_dictionary = {}
list_bid = []  

def find_highest_bidder(bid_dictionary):
    for key in bid_dictionary:
        list_bid.append(bid_dictionary[key])
    print(list_bid)

    # program to find largest number in a list
    max = list_bid[0]
    for num in list_bid:
        if num > max:
            max = num
    # print(max)
    for key in bid_dictionary:
        if bid_dictionary[key] == max:
            print(f"{key} wins the bid with the bidding amount of {max}")

while is_user:
    username = input("Enter your name\n")

    bidding_amount = int(input("Enter your bidding amount\n"))

    next_user = input("Are there more users?? Press Yes to continue or No to stop the bidding\n")

    bid_dictionary[username] = bidding_amount
    if(next_user) == "Yes":
        clear()
        continue
    else:
        is_user = False
        clear()
        find_highest_bidder(bid_dictionary)
     


