import Tools
from Tools import addmember

filik = 'user_ids.txt'
stroka = '\n' + '16476748'

addmember(filik, stroka)

with open(filik, 'r') as f:
    for line in f:
        print(line)