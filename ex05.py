
# compare intersection of given lists

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a_set = set(a)
b_set = set(b)

combine = a_set.intersection(b_set)

print(list(combine))

# alternate method
commonList = set()
[commonList.add(x) for x in a for y in b if x == y]
print(commonList)

# randomly generate two lists and identify intersection

import random as r

c = r.sample(range(1,20), r.randint(1,10))
d = r.sample(range(1,30), r.randint(1,20))

c_set = set(c)
d_set = set(d)
combine2 = c_set.intersection(d_set)
print(combine2)