#Get input from user & convert into integers (in decimal)
INPUT = input("Enter number to convert to binary: ")
binary = 0
num = int(INPUT)

#Convert into binary




if (num - 1024) >= 0:
    binary = binary + 10000000000
    num = num - 1024
else:
    binary = binary
    num = num

if (num - 512) >= 0:
    binary = binary + 1000000000
    num = num - 512
else:
    binary = binary
    num = num

if (num - 256) >= 0:
    binary = binary + 100000000
    num = num - 256
else:
    binary = binary
    num = num

if (num - 128) >= 0:
    binary = binary + 10000000
    num = num - 128
else:
    binary = binary
    num = num

if (num - 64) >= 0:
    binary = binary + 1000000
    num = num - 64
else:
    binary = binary
    num = num

if (num - 32) >= 0:
    binary = binary + 100000
    num = num - 32
else:
    binary = binary
    num = num

if (num - 16) >= 0:
    binary = binary + 10000
    num = num - 16
else:
    binary = binary
    num = num

if (num - 8) >= 0:
    binary = binary + 1000
    num = num - 8
else:
    binary = binary
    num = num

if (num - 4) >= 0:
    binary = binary + 100
    num = num - 4
else:
    binary = binary
    num = num

if (num - 4) >= 0:
    binary = binary + 100
    num = num - 4
else:
    binary = binary
    num = num

if (num - 2) >= 0:
    binary = binary + 10
    num = num - 2
else:
    binary = binary
    num = num

if (num - 1) >=0:
    binary = binary + 1
    num = num - 1
else:
    binary = binary
    num = num


#Print
print("The number " + str(INPUT) + " converted to binary is: " + str(binary))