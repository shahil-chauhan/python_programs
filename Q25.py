# With two given lists [1,3,6,78,35,55] and
# [12,24,35,24,88,120,155], write a program to make a
# list whose elements are intersection of the above given lists.


lst1 = [1, 3, 6, 78, 35, 55]
lst2 = [12, 24, 35, 24, 88, 120, 155]

# convert them to set
set1 = set(lst1)
set2 = set(lst2)

# set method for intersecton
intersection = set.intersection(set1, set2)

print(intersection)
