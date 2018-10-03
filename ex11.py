
def primeCheck(x):
    # x = int(input(help_text))
    n = x//2
    if x == 1 or x == 2 or x == 3:
        result = True
    else:
        for num in range(2,n+1):
            if x % num == 0:
                result = False
                break
            result = True
    return result


# testing

for num in range(1,12):
    print(num, 'is prime?', primeCheck(num))
