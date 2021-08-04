# Write a program which are divisible by 7 and
# between a given range 0 and n.

number = int(input('Enter the Range: '))

for num in range(1, number+1):
    if num % 7 == 0:
        print(num)
