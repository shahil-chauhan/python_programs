# Write a program to generate below Pattern:

# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

def pypart(n):

    # outer loop to handle number of rows
    for i in range(n, 0, -1):

        for j in range(0, (n+1)-i):
            print(" ", end="")

        # inner loop to handle number of columns
        for j in range(0, i):

            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")


# Driver Code
num = int(input('Enter num of rows : '))
pypart(num)
