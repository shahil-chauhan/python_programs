#  Write a program that computes the value of
# a+aa+aaa+aaaa with a given digit as the value of a.

num = input("Enter a number:")

result = 0
for digit in range(1, 5):
    result = result + int(str(num*digit))

print(result)
