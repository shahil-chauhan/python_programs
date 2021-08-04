# By using list comprehension, please write a program to
# print the list after removing delete numbers which are
# divisible by 5 and 7 in [12,24,35,70,88,120,155].

# given list
li = [12, 24, 35, 70, 88, 120, 155]

# driver code
lst = [num for num in li if (num % 5 != 0) and (num % 7 != 0)]

print(lst)
