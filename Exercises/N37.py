lista = []
for i in range(100):
    char = input()
    lista.append(char)

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
for i in lista:
    if i == 'a':
        count_a += 1
    elif i == 'e':
        count_e += 1
    elif i == 'i':
        count_i += 1
    elif i == 'o':
        count_o += 1
    elif i == 'u':
        count_u += 1

flag = False

if count_a > 0 and count_e + count_i + count_o + count_u == 0:
    flag = True
elif count_e > 0 and count_a + count_i + count_o + count_u == 0:
    flag = True
elif count_i > 0 and count_a + count_e + count_o + count_u == 0:
    flag = True
elif count_o > 0 and count_a + count_i + count_e + count_u == 0:
    flag = True
elif count_u > 0 and count_a + count_i + count_o + count_e == 0:
    flag = True


if not flag:
    print('ERRORE', end='')
else:
    print('OK', end='')