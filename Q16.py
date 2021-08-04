#  Please write a program to randomly generate a list
# with 5 even numbers between 100 and 200 inclusive.

import random

# driver code
lst = [num for num in range(100, 201) if num % 2 == 0]
output = random.sample(lst, 5)

# output
print(output)
