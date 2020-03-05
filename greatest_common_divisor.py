# code to compute the greatest common divisor (GCD, or highest common factor) of two positive integers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = 0
if num1 > num2:
    big = num1
else:
    big = num2

for i in range(1, big):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print("The greatest common divisor is: " + str(gcd))