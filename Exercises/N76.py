def prendi_tabella(m,n):
    tabella = []
    riga = []
    for _ in range(m):
        for _ in range(n):
            riga.append(int(input()))
        tabella.append(riga)
        riga = []
    return tabella

def conta_voti_maggiori_5(lista):
    count = 0
    for i in lista:
        if i > 5:
            count += 1
    return count

def somma_colonna(tabella, m,n):
    lista_voti_cantanti = []
    somma = 0
    for j in range(n):
        for i in range(m):
            somma += tabella[i][j]
        lista_voti_cantanti.append(somma)
        somma = 0
    return lista_voti_cantanti

def cerca_peggiore(lista):
    peggiore = 0
    for i in range(len(lista)):
        if lista[i] <= lista[peggiore]:
            peggiore = i
    return peggiore

def punto_a(tabella):
    piu_buono = 0
    for i in range(1, len(tabella)):
        if conta_voti_maggiori_5(tabella[i]) >= conta_voti_maggiori_5(tabella[piu_buono]):
            piu_buono = i
    return piu_buono

def punto_b(tabella, m,n):
    lista = somma_colonna(tabella, m,n,)
    peggiore = cerca_peggiore(lista)
    return peggiore
    


def main():
    m = int(input())
    n = int(input())
    tabella = prendi_tabella(m,n)
    print(punto_a(tabella), punto_b(tabella, m, n), end='')

main()