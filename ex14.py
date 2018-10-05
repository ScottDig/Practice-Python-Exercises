# List Remove Duplicates



def removeListDups(lst):
    newlst = []
    while bool(len(lst)):
        x = lst.pop()
        if x not in newlst:
            newlst.append(x)
    newlst.sort()
    return newlst

a = [1, 2, 3, 4, 4, 4, 1, 2, 5, 6, 2]

print(removeListDups(a))
