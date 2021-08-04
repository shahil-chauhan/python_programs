# Write a program that accepts a sentence and calculate
# the number of uppercase letters and lowercase letters.

sen = input("Enter a sentence : ")

upper = 0
lower = 0

for char in sen:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    else:
        continue

print(f'Number of uppercase letters:{upper}')
print(f'Number of lowercase letters:{lower}')
