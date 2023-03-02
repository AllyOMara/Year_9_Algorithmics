'''
This program will calculate the greatest common divisor of two 
positive integers given by the user, using Eculid's Algorithm.
'''

# 1. Get input from user
input1 = input("Enter first number: ")
input2 = input("Enter second number: ")
num1 = int(input1)
num2 = int(input2)

# 2. Calculate gcd
while (num1 != 0 or num2 != 0) and (num1 > 0 and num2 > 0):
    # Minus the bigger number from the smaller number, repeat this until one is zero
    if num1 > num2:
        num1 = num1 - num2
    else:
        num2 = num2 - num1

if num1 == 0:
    result = num2
else:
    result = num1

# 3. Print the result
#print("The gcd of " + input1 + " and " + input2 + " is: " + str(result))

print(f"The gcd of {input1} and {input2} is : {result}")

