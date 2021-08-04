# Please write a program to generate a list with 5 random
# numbers between 100 and 200 inclusive.


import random

# driver code
lst = [num for num in range(100, 201)]
output = random.sample(lst, 5)

# output
print(output)
