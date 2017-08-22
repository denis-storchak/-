import Tools
from Tools import addmember

num = ''
user_amount = int(input('¬ведите кол-во новых участников: '))
codes = []

with open('Registration_ids.txt', 'r') as f:
    for line in f:
        codes.append(line.strip())

for i in range(user_amount):
    filik = 'codenames.txt'
    num = codes[i]
    stroka = '\n' + num + ' ' + input()
    addmember(filik, stroka)