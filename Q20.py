# Please write a program to print the list after
# removing delete even numbers in [5,6,77,45,22,12,24].


#given list
lst = [5, 6, 77, 45, 22, 12, 24]

#driver code
num = list(filter(lambda x: x % 2 != 0, lst))

#output
print(num)
