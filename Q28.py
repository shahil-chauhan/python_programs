# By using list comprehension, please write a program to print
# the list after removing the 0th, 2nd, 4th,6th numbers in
# [12,24,35,70,88,120,155].


ori_lst = [12, 24, 35, 70, 88, 120, 155]

# driver code
new_lst = [j for i, j in enumerate(ori_lst) if i % 2 != 0 and i <= 6]

# output
print(new_lst)
