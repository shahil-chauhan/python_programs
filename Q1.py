#write a script that prints the multiples of 7 
# between 0 and 100

for num in range(1, 101):
    if num % 7 == 0:
        print(num, end=' ')
