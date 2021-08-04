# write a program to output a random number,
# which is divisible by 5 and 7, between 0 and 10
# inclusive using random module and list comprehension.

import random

#user input
begin = int(input("Start :"))
end = int(input("End : "))

#list comprehension 
lst = [num for num in range(begin, end) if (num % 5 == 0) and (num % 7 == 0)]

output = random.sample(lst, 1)

print(output)
