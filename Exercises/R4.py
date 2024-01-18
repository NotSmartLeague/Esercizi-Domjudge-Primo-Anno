def prendi_lista():
    lista = []
    n = int(input())
    for _ in range(n):
        elemento = int(input())
        lista.append(elemento)
    return lista

def cerca_ricorrenze(lista, x):
    ricorrenze = []
    for i in range(len(lista)):
        if lista[i] == x:
            ricorrenze.append(i)
    return ricorrenze

def sostituisci(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            lista[i] = 0
    return lista

def trova_intero(lista, ricorrenze, x, c):
    if c == 0:
        return x
    ricorrenze = cerca_ricorrenze(lista, x)
    nuova_lista = sostituisci(lista, x)
    c = len(ricorrenze)
    x = c
    return x + trova_intero(nuova_lista, ricorrenze, x, c)

def main():
    x = int(input())
    lista = prendi_lista()
    ricorrenze = cerca_ricorrenze(lista,x)
    c = len(ricorrenze)
    if ricorrenze:
        n = trova_intero(lista, ricorrenze, x, c)
        print(n, end='')
    else:
        print(c, end='')

    
    
main()

