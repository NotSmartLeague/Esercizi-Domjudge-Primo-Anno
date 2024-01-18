def media_lista(lista):
    if len(lista) > 0:
        somma = 0
        for i in lista:
            somma += i
        media = somma // len(lista)
        return media
    else:
        return 0
def input_lista():
    lista = []
    while True:
        n = int(input())
        if n != -50:
            lista.append(n)
        else:
            break

    return lista

def main():
    lista = input_lista()
    media = media_lista(lista)
    min = 1001
    if len(lista) > 0:
        for i in lista:
            if i >= media and i < min:
                    min = i
    if not lista:
        print('VUOTA', end='')
    else:
        print(min, end='')

main()