# Please write a program to randomly generate a
# list with 5 numbers, which are divisible by 5 and 7 ,
# between 1 and 1000 inclusive.


import random

# driver code
lst = [num for num in range(1, 1001) if (num % 5 == 0) and (num % 7 == 0)]
output = random.sample(lst, 5)

# output
print(output)
