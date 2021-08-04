# Write a program which accepts a sequence of
# comma-separated numbers from the console and
# generate a list and a tuple which contains every
# number.

number = input('Enter the numbers : ')

list = number.split(',')
tuple = tuple(list)

print(list)
print(tuple)
