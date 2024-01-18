def crea_matrice():
    matrice = []
    n = int(input())
    for i in range(n):
        lista = []
        for j in range(n):
            lista.append(int(input()))
        matrice.append(lista)
    
    return matrice

def verifica(matrice):
    indice = len(matrice) // 2
    somma_croce = 0
    somma_elementi = 0
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if j != indice and i != indice:
                somma_elementi += matrice[i][j]
            elif i == indice or j == indice:
                somma_croce += matrice[i][j]
    if somma_croce > somma_elementi:
        return True
    else:
        return False


def main():
    matrice = crea_matrice()
    if verifica(matrice):
        print('OK', end='')
    else:
        print('NO', end='')

main()