# Please write a program which accepts a string from the console
# and prints it in reverse order.
# If the following string is given as input to the program:
# rise to vote sir
# Then, the output of the program should be:
# ris etov ot esir


# reverse function
def rev(x):
    return x[::-1]


# string input
inp_str = input("Enter a string to reverse: ")

# function call
rev_str = rev(inp_str)

print(rev_str)
