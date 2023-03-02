'''
This program will calculate and print the quotent and remainder of two numbers.
'''

# 1. Get input from user
input1 = input("Enter first number: ")
input2 = input("Enter second number: ")
num1 = int(input1)
num2 = int(input2)
count = 0

#Define Variables
if num1 > num2:
    remainder = num1
    smaller_number = num2
if num2 > num1:
    remainder = num2
    smaller_number = num1

# 2. Calculate the quotent and remainder
while (remainder > smaller_number):
    count = count + 1
    remainder = remainder - smaller_number

# 3. Print the result

print("the answer is:", count, "remainder", remainder)

