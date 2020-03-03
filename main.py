# weight = float(input("Enter your weight: "))
# height = float(input("Enter your height: "))
# bmi = weight / (height * height)
# bmi1 = weight / (height ** 2)
# bmi2 = weight / math.pow(height, 2) 
# print("Your BMI is " + str(bmi))
# print("Your BMI1 is " + str(bmi1))
# print("Your BMI2 is " + str(bmi2)

# # Prompt user to enter starting year
# start_year = int(input("What year do you want to start with? "))
# # Prompt user to enter the number of years to be checked
# number_of_years = int(input("How many years do you want to check? "))
# end_year = start_year + number_of_years
# # For leap years, year must be evenly divisible by 4. Not a leap year if evenly divisible by 100 unless also by 400
# for i in range(start_year, end_year):
#     if start_year % 4 == 0:
#         if start_year % 100 == 0:
#           if start_year % 400 == 0:
#             print('Year: ' + str(start_year) + ' is a leap year')
#           else:
#             print('Year: ' + str(start_year) + ' is not a leap year')
#         else:
#           print('Year: ' + str(start_year) + ' is a leap year')
#     else:
#       print('Year: ' + str(start_year) + ' is not a leap year')

# Prompt user to enter starting year
start_year = int(input("What year do you want to start with? "))
# Prompt user to enter the number of years to be checked
number_of_years = int(input("How many years do you want to check? "))
end_year = start_year + number_of_years
# For leap years, year must be evenly divisible by 4. Not a leap year if evenly divisible by 100 unless also by 400
for i in range(start_year, end_year):
    if i % 4 == 0:
        if i % 100 == 0:
          if i % 400 == 0:
            print('Year: ' + str(i) + ' is a leap year')
          else:
            print('Year: ' + str(i) + ' is not a leap year')
        else:
          print('Year: ' + str(i) + ' is a leap year')
    else:
      print('Year: ' + str(i) + ' is not a leap year')
          