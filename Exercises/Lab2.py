def prendi_liste(n):
    lista1 = []
    lista2 = []
    for _ in range(n):
        lista1.append(int(input()))
    for _ in range(n):
        lista2.append(int(input()))
    
    return lista1, lista2

def controlla_distinti(numeratore, denominatore, lista):
    frazione = [numeratore, denominatore]
    for i in lista:
        if i[0] == frazione[0] and i[1] == frazione[1]:
            return False
    return True



def controlla(lista1, lista2, n):
    ripetuti = []
    cont = 0
    for numeratore in lista1:
        for denominatore in lista2:
            if numeratore % denominatore == 0 and controlla_distinti(numeratore, denominatore, ripetuti):
                cont += 1
            ripetuti.append([numeratore, denominatore])
    return cont == n

def main():
    n = int(input())
    lista1, lista2 = prendi_liste(n)
    if controlla(lista1, lista2, n):
        print('SI', end='')
    else:
        print('NO', end='')

main()