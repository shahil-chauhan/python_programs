# With a given integral number n,
# write a program to generate a dictionary
# that contains (i, i*i) such that is an integral
# number between 1 and n (both included). and then
# the program should print the dictionary.

number = int(input('Enter the number: '))

my_dict = {num: num*num for num in range(1, number+1)}

print(my_dict)
