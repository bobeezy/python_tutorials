number = int(input("Enter a number: "))
answer = number + 10
print(str(number) + " + 10 = " + str(answer))

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight / (height * height)
bmi1 = weight / (height ** 2)
bmi2 = weight / math.pow(height, 2) 
print("Your BMI is " + str(bmi))
print("Your BMI1 is " + str(bmi1))
print("Your BMI2 is " + str(bmi2)
