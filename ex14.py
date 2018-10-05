# List Remove Duplicates



def removeListDups1(lst):
    newlst = []
    while bool(len(lst)):
        x = lst.pop()
        if x not in newlst:
            newlst.append(x)
    newlst.sort()
    return newlst


def removeListDups2(lst):
    newlst = []
    for x in lst:
        if x not in newlst:
            newlst.append(x)
    newlst.sort()
    return newlst


def removeListDups3(lst):
    newlst = list(set(lst))
    return newlst


a = [1, 2, 3, 4, 4, 4, 1, 2, 5, 6, 2]
print(removeListDups1(a))
a = [1, 2, 3, 4, 4, 4, 1, 2, 5, 6, 2]
print(removeListDups2(a))
a = [1, 2, 3, 4, 4, 4, 1, 2, 5, 6, 2]
print(removeListDups3(a))
