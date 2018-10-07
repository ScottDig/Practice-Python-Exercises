
string = input('input a handful of words: ')

def reverseString(string):
    # reverses word order of a string
    lst = string.split()
    lst.reverse()
    return ' '.join(lst)

print(reverseString(string))
