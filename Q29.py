#  By using list comprehension, please write a program to print
# the list after removing the 0th,4th,5th numbers
# in [12,24,35,70,88,120,155.


ori_lst = [12, 24, 35, 70, 88, 120, 155]
indices = [0, 4, 5]

# driver code
new_lst = [j for i, j in enumerate(ori_lst) if i not in indices]

# output
print(new_lst)
