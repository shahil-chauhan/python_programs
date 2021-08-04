# Write a program to print the below pattern

# 	       *
# 	     * *
#      * * *
#    * * * *
#  * * * * *


# function to print the pattern
def pypart(n):

    # outer loop to handle number of rows
    for i in range(0, n):

        for j in range(0, (n+1)-i):
            print("  ", end="")

        # inner loop to handle number of columns
        for j in range(0, i+1):

            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")


# Driver Code
num = int(input('Enter num of rows : '))
pypart(num)
