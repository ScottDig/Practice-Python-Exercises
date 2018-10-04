
def fibo(number):
    lst = []
    for num in range(number):
        if num == 0 or num == 1:
            lst.append(1)
        else:
            lst.append(lst[num-2]+lst[num-1])
    return lst





fibo(3)
fibo(4)
