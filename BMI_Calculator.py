weight_inkg = float(input("Enter your weight in kgs: "))
height_inmtrs = float(input("Enter your height in meters: "))
print(type(weight_inkg))
print(type(height_inmtrs))



BMI_float= weight_inkg/height_inmtrs ** 2
BMI = int(BMI_float)
print("Your BMI is : " + str(BMI))

if(BMI_float < 18.5):
    print("You are underweight.")

elif(BMI_float > 18.5 and BMI_float < 25):
    print("You have a normal weight.")

elif(BMI_float > 25 and BMI_float < 30):
    print("You have a overweight.")

elif(BMI_float > 30 and BMI_float < 35):
    print("You have a obese.")

else:
    print("You are clinically obese.")