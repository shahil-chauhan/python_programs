# Write a program which can compute the factorial of
# a given numbers.The results should be printed in a
# comma-separated sequence on a single line.


#function defination
def factorial(num):
    return 1 if (num == 1) or (num == 0) else num * factorial(num - 1)

# driver code
number = int(input('Enter the number: '))

#print with the function call
print(factorial(number))
