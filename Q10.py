'''
You are required to write a program to sort the (name, age, height) 
tuples by ascending order where name is string, age and height are 
numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
'''

people_info = []

while True:
    info = input('Enter the (name,age,height): ')

    if info == '':
        break
    else:
        people_info.append(tuple(info.split(',')))
        people_info.sort(key=lambda nxt: (nxt[0], nxt[1], nxt[2]))

print(people_info)