
string1 = input('Enter a word: ')
check = None

for index, letter in enumerate(string1, start=1):
    if string1[index-1] != string1[-index]:
        check = 'fail'
        print(string1, 'is not a palidrome')
        break

if check is None:
    print(string1, 'is a palindrome')