# Program that encodes a message of any length by a single-word cipher inputted by the user.

import sys
from cs50 import get_string

# Ensure cipher is entered
if len(sys.argv) != 2:
    print("Enter Valid Cipher")
    sys.exit(1)

# Ensure cipher contains only letters
if str.isalpha(sys.argv[1]):
    cipher = sys.argv[1]
else:
    print("not valid")
    sys.exit(1)

# Get Input from user
plaintext = get_string("Enter Plaintext Now: ")
print("ciphertext: ")

# Iterate through each character in plaintext & modify it by the "j"th character of cipher
j = 0
for c in plaintext:
    # Modify all alphabetical characters of plaintext by cypher
    if str.isalpha(c):
        # Find Value for key1 and case
        plainchar = ord(c)
        if str.isupper(c):
            key1 = plainchar - 65
            case = 65
        else:
            key1 = plainchar - 97
            case = 97
        # Find value for new_key
        cipherchar = ord(cipher[j])
        if str.isupper(cipher[j]):
            new_key = cipherchar - 65
        else:
            new_key = cipherchar - 97
        # Plug values into euqation to get an encoded character
        ciphertext = chr(((key1 + new_key) % 26) + case)
        print(ciphertext, end="")
        j += 1
        if j == len(cipher):
            j = 0
    else:
        print(c, end="")

print("")
