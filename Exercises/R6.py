def prendi_matrice():
    n = int(input())
    lista = []
    matrice = []
    for i in range(n):
        for j in range(n):
            elemento = int(input())
            lista.append(elemento)
        matrice.append(lista)
        lista = []
    return matrice

def verifica(matrice, min, max, x, y):
    #CASO BASE 1, quando la funzione arriva alla fine della diagonale secondaria,
    # vuol dire che i casi fino ad ora sono stati verificati positivamente, quindi
    # ritorna si
    if x == 0 and y == len(matrice) - 1:
        return 'SI'
    somma = 0
    #somma colonna
    for i in range(0, max + 1):
        somma += matrice[i][min]
    #somma riga
    for j in range(min + 1, len(matrice)):
        somma += matrice[i][j]
    #CASO RICORSIVO, se la somma della L è divisibile per l'angolo della l,
    #richiama la funzione, modificando i parametri come segue per spostarsi alla prossima L
    if somma % matrice[x][y] == 0:
        return verifica(matrice, min + 1, max - 1, x - 1, y + 1)
    #se non è divisibile si può ritornare direttamente NO
    else:
        return 'NO'
  
def main():
    matrice = prendi_matrice()
    print(verifica(matrice, min=0, max=len(matrice) - 1, x=len(matrice) - 1, y=0), end='')

main()