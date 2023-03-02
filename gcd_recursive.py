def gcd(num1, num2):
    """Recursively calculate the greatest common devisor (gcd) of two integers

    Args:
        num1 (_type_): first integer
        num2 (_type_): second integer

    Returns:
        _type_: integer representing gcd of num1 and num2
    """
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)
                
answer = gcd(21, 9)

print("Recurive solution: " + str(answer))