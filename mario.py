from cs50 import get_int

# Prompt user for blocks, 0-23
while True:
    h = get_int("Positive number: ")
    if h > -1 and h < 24:
        break

# Print out this many rows
for i in range(h):

    # Print the appropriate number of spaces, left blocks, 2 spaces, and right blocks
    for k in range(i+1, h):
        print(" ", end="")

    for j in range(h-i-1, h):
        print("#", end="")

    print("  ", end="")

    for l in range (h-i-1, h):
        print("#", end="")
    # Print a new line
    print()