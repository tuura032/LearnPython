# Takes input of a credit card number, and if input is valid, determines if it is a valid credit number

from cs50 import get_int

# Prompt user for CC number
while True:
    cc = get_int("CC number: ")
    if cc > 99999999:
        break

cccopy = cc

# CC number minus last digit
nolast = cc//10

# Set Counter to 2nd to last digit, possibly x2
initialcounter = ((nolast%10)*2)

if initialcounter > 9:
    counter = (initialcounter%10)+1
else:
    counter = initialcounter

# Add Together every other digit from cc, possibly x2
while True:
    if nolast == 0:
        break
    nolast = nolast//100
    k = ((nolast%10)*2)
    if k > 9:
        k = (k%10)+1
    for x in range(k):
        counter += 1

# Add together all remaining digits from cc
counter2 = cc % 10
while True:
    if cccopy == 0:
        break
    cccopy = cccopy//100
    m = cccopy % 10
    for y in range(m):
        counter2 += 1

# Add Values together in Checksum
sum1 = counter + counter2

# Determine which card type if valid
if ((sum1 % 10) > 0) or ((sum1 % 10) < 0):
    print("INVALID")
else:
    if (cc // 1000000000000) == 4 or (cc // 1000000000000000) == 4:
        print("VISA")
    elif (cc // 10000000000000) == 34 or (cc // 10000000000000) == 37:
        print("AMEX")
    elif (cc // 100000000000000) > 50 and (cc // 100000000000000) < 56:
        print("MASTERCARD")
    else:
        print("INVALID")
