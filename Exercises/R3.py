def prendi_matrice():
    n = int(input())
    lista = []
    matrice = []
    for _ in range(n):
        for _ in range(n):
            elemento = int(input())
            lista.append(elemento)
        matrice.append(lista)
        lista = []
    return matrice

def somma_iterativa(matrice):
    somma = 0
    j = len(matrice) - 1
    for i in range(len(matrice)):
        somma += matrice[i][j]
        j -= 1
    return somma

def somma_ricorsiva(matrice, i, j, somma):
    somma += matrice[i][j]
    if j == 0:
        return somma
    return somma_ricorsiva(matrice, i + 1, j - 1, somma)

def main():
    matrice = prendi_matrice()
    somma_i = somma_iterativa(matrice)
    somma_r = somma_ricorsiva(matrice,0,len(matrice) - 1,0)
    print(somma_i,somma_r, end='',sep=';')

main()