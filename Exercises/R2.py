#FUNZIONE PER PRENDERE LISTA DI N ELEMENTI
def prendi_lista():
    n = int(input())
    lista = []
    for i in range(n):
        lista.append(int(input()))
    return lista

#FUNZIONE RICORSIVA
def verifica(lista, i, j):
    #PRIMO CASO BASE, se la lunghezza della lista è dispari, ritorna no
    if len(lista) % 2 != 0:
        return 'NO'
    #SECONDO CASO BASE, se il contatore j arriva alla fine senza mai uscire vuol dire
    # che tutti gli elementi della prima metà sono uguali a quelli della seconda metà
    elif i == len(lista) // 2:
        return 'SI'
    #CASO RICORSIVO, se l'elemento della prima lista è uguale all'elemento di indice corrispondente della seconda lista
    # richiama la funzione
    elif lista[i] == lista[j]:
        return verifica(lista, i + 1, j + 1)
    #TERZO CASO BASE, se anche solo una coppia di elementi non è uguale, ritorna semplicemente no
    else:
        return 'NO'

def main():
    lista = prendi_lista()
    #si chiama la funzione con parametro i == 0 e parametro j == alla metà della lunghezza della lista
    print(verifica(lista,0, len(lista) // 2), end='')

main()
