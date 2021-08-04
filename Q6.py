# Write a program that accepts sequence of lines as
# input and prints the lines after making all characters
# in the sentence capitalized.

lines = []

while True:
    line = input('Enter line: ')
    if line:
        lines.append(line.upper())
    else:
        break

for line in lines:
    print(line)
