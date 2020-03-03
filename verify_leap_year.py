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