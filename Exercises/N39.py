from math import log2


def is_sqrt(n):
    log_n = log2(n)
    if log_n.is_integer():
        #print('il log2 di', n, 'è', log_n,'ed è intero')
        return True
    else:
        #print('il log2 di', n, 'è', log_n,'e non è intero')    
        return False

count = 0
potenze = 0

while True:
    n = int(input())
    if n == 0:
        break
    else:
        if is_sqrt(n):
            #print(n, 'è una potenza di 2')
            potenze += 1
        else:
            #print(n, 'non è un potenza di 2')
            ...
        count += 1


if count == potenze:
    print('SI', end='')
else:
    print('NO', end='')


