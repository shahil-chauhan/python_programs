# Please write a program to generate all sentences where
# the subject is in ["I", "You"] and verb is in ["Play", "Love"]
# and the object is in ["Hockey","Football"].

subject = ["I", "You"]
verb = ["Play", "Love"]
object = ["Hockey", "Football"]

# to iterate through the lists
for sub in subject:
    for ver in verb:
        for obj in object:
            print(f'{sub} {ver} {obj}')
