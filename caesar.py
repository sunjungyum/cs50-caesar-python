# Sun-Jung Yum
# Problem Set 6
# 25 October 2018

import sys
from cs50 import get_string

# Ensures that the usage is correct
if len(sys.argv) != 2:
    sys.exit("Usage: python caesar.py k")

# Declares an int variable for the key
key = int(sys.argv[1])

# Prompts for the plain text
plaintext = get_string("plaintext: ")
print("ciphertext: ", end="")

# Iterates through each character of the plain text
for c in plaintext:
    if c.isalpha():
        # Rotates characters as uppercase characters
        upper = c.upper()
        alphabeticalindex = ord(upper) - 65
        # Uses a separate variable called "result" because c's case needs to be checked
        result = 65 + ((alphabeticalindex + key) % 26)

        # Converts it back to a char (if original was lowercase, returns back to lowercase)
        if c.islower():
            c = chr(result).lower()
        else:
            c = chr(result)

    # Prints either the alphabetical rotated character or the nonalphabetical character as is
    print(c, end="")

# Prints empty line
print("")