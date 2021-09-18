#formula --> (150.00/5) * 1.12


#formula --> totalbill/no of people) * (percenatge/100+1)


total_bill = float(input("Enter the total bill: "))

No_of_people = int(input("No. of People: "))

Tip_Percentage = int(input("Tip Percentage : "))

Pay_per_person = round((total_bill/No_of_people) * (Tip_Percentage/100 + 1),2)

print(f"Each person should pay {Pay_per_person}")