
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for num in a:
    if num < 5:
        print(num)
        b.append(num)

print(b)


# researched solutions below

# single line solution
print(list(filter(lambda x:x < 5, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])))

# single line solution
print([x for x in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if x <=5])