# With a given list [12,24,35,24,88,120,155,88,120,155],
# write a program to print this list after removing all
# duplicate values with original order reserved.

def dupl(li):
    new_lst = []
    [new_lst.append(i) for i in li if i not in new_lst]
    # for i in li:
    #     if i not in new_lst:
    #         new_lst.append(i)

    print(new_lst)


lst = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

dupl(lst)
