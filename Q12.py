# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.

number = input('Enter : ')

output = [int(num)**2 for num in number.split(',') if (int(num) % 2 != 0)]

print(output)
