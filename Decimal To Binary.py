# Helper Functions

def getPower(strLocation, strLength):
    return strLength - strLocation - 1

def caluclatePowerOfTwo(power):
    return 2**power

# Get input from user
#userInput = input("Enter number to convert to binary: ")
userInput = "3"

inputLength = len(userInput)
binaryOutput = ""
binaryLength = 4 # Length of binary string
 
# Convert input from string to integer
userInputAsDec = int(userInput)

binaryRef = 0
# Convert input to binary
while binaryRef < binaryLength:
    
    # Check if the binaryRef position will divide into userInput
    power = getPower(binaryRef, binaryLength)
    integerAmt = caluclatePowerOfTwo(power)

    if userInputAsDec // integerAmt != 0:
    #if userInputAsDec - integerAmt >= 0:
        binaryOutput += "1" 
    else:
        binaryOutput += "0" 

    binaryRef += 1

print(binaryOutput)
