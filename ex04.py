

def divisors(integer):
    integer = abs(integer)
    divisor = []
    for candidate in range(integer//2):
        if integer % (candidate+1) == 0:
            divisor.append(candidate+1)
    return divisor

alist = divisors(10)

print(alist)