# random password generator

import random as rd
import json
import random

# using dictionary.json file (stored locally) from https://github.com/adambom/dictionary
f = open("dictionary.json")
word_dict = json.load(f)
f.close()
word_list = list(word_dict.keys())

w1 = word_list[random.randint(0, len(word_list))]
w2 = word_list[random.randint(0, len(word_list))]
n1 = random.randint(0,100)

simple_password = w1 + w2 + str(n1)
print(simple_password)

uletters = ' A B C D E F G H I J K L M N O P Q R S T U V W X Y Z '
lletters = ' a b c d e f g h i j k l m n o p q r s t u v w x y z '
symbols = ' ! @ # $ % ^ & * - _ '
numbers = ' 0 1 2 3 4 5 6 7 8 9 '
characters = (uletters + lletters + symbols + numbers).split()

hard_password = ''
for i in range(15):
    hard_password = hard_password + characters[random.randint(0, len(characters))]

print(hard_password)
