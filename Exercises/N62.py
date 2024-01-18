def prendi_input():
    k = int(input())
    lista = []
    for i in range(k):
        lista.append(int(input()))
    n = int(input())
    m = int(input())

    return lista,n,m

def crea_matrice(n,m):
    matrice = []
    for i in range(n):
        matrice.append([0]*m)
    
    return matrice

def assegna_elementi(matrice, m , n, lista,i,j, min_i, min_j, capienza,cont, max):
    """
                i             |       j
       1. min_i --> min_i     | min_j --> m
       2. min_i + 1 --> n     | m --> m
       3. n --> n             | m - 1 --> min_j
       4. n - 1 --> min_i + 1 | min_j --> min_j
    """
    #caso base:
    if capienza == max:
        return matrice
    
    #step 1
    for j in range(min_j, m):
        matrice[min_i][j] = lista[cont]
        capienza += 1
        cont += 1
        if capienza == max:
            return matrice
        if cont == len(lista):
            cont = 0


    #step 2
    for i in range(min_i + 1, n):
        matrice[i][m - 1] = lista[cont]
        capienza += 1   
        cont += 1
        if capienza == max:
            return matrice
        if cont == len(lista):
            cont = 0

    #step 3
    for j in range(m - 2, min_j - 1, -1):
        matrice[n - 1][j] = lista[cont]
        capienza += 1
        cont += 1
        if capienza == max:
            return matrice
        if cont == len(lista):
            cont = 0

    #step 4
    for i in range(n - 2, min_i, -1):
        matrice[i][min_j] = lista[cont]
        capienza += 1
        cont += 1
        if capienza == max:
            return matrice
        if cont == len(lista):
            cont = 0
    
    return assegna_elementi(matrice=matrice, m=m-1, n=n-1, lista=lista, i=i, j=j, min_i=min_i+1, min_j=min_j+1, capienza=capienza,max=max, cont=cont)



def stampa_matrice(matrice):

    for i in matrice:
        for j in i:
            print(j, end='')
        print()
    


def main():
    lista,n,m = prendi_input()
    matrice = crea_matrice(n,m)
    nuova_matrice = assegna_elementi(matrice=matrice, m = m , n = n, lista = lista,i=0,j=0, min_i=0, min_j=0, capienza=0,cont=0, max=n*m)
    stampa_matrice(nuova_matrice)

main()


