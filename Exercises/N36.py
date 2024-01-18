lista = []

for i in range(10):
    num = int(input())
    lista.append(num)

x = int(input())


divisibile = False
for i in lista:
    if i % x == 0 and i != 0:
        divisibile = True
        #print(i, 'è divisibile')
        break
    # else:
        print(i, 'non è divisibile')

if divisibile:
    print('NO', end='')
else:
    print('OK', end='')

