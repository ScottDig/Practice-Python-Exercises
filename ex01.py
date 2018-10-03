import datetime
Today = datetime.datetime.today()
Year = Today.year

Name = input('Hello. What is your name? ')
Age = int(input("What is your age? "))
age_index = input('Did you have your birthday this year? (Y/N): ').upper()

if age_index == 'Y':
    base = 100
elif age_index == 'N':
    base = 99
try:
    print(Name + ' you will turn 100 in the year ' + str(Year + base - Age))
except NameError:
    print(Name + ' ,you did not enter "Y" or "N".')


