def prendi_lista():
    lista = []
    x = int(input())
    for i in range(x):
        lista.append(int(input()))
    return lista

def dividi(lista):
    pari = []
    dispari = []
    for i in range(len(lista)):
        if i % 2 == 0:
            pari.append(lista[i])
        else:
            dispari.append(lista[i])
    return pari, dispari

def controlla_pari(pari):
    for i in range(len(pari) - 1):
        j = i + 1
        if pari[i] >= pari[j]: 
            return False
    return True

def controlla_dispari(dispari):
    for i in dispari:
        if i % 2 == 0:
            return False
    return True

def main():
    lista = prendi_lista()
    pari, dispari = dividi(lista)
    punto_1 = controlla_pari(pari)
    punto_2 = controlla_dispari(dispari)
    if punto_1 and punto_2:
        print('SI', end='')
    else:
        print('NO', end='')


main()