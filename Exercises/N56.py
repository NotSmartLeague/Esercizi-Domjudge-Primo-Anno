def init_matrice(dim):
    matrice = []
    for i in range(dim):
        matrice.append([0] * dim)
    return matrice

def prendi_comandi():
    lista_comandi = []
    i = 0
    # stampa_menu()
    comando = int(input())
    while i < 100 and comando != 9:
        lista_comandi.append(comando)
        # stampa_menu()
        comando = int(input())
    return lista_comandi

def esegui_comandi(lista_comandi, i, matrice, x, y, penna):
    if i == len(lista_comandi):
        return matrice
    if lista_comandi[i] == 1:
        penna = alza_penna(penna)
    elif lista_comandi[i] == 2:
        penna = abassa_penna(penna)  
    elif lista_comandi[i] == 3:
        matrice, x, y, = vai_est(matrice, x, y, penna)
    elif lista_comandi[i] == 4:
        matrice, x, y, = vai_ovest(matrice, x, y, penna)  
    elif lista_comandi[i] == 5:
        matrice, x, y, = vai_sud(matrice, x, y, penna)
    elif lista_comandi[i] == 6:
        matrice, x, y, = vai_nord(matrice, x, y, penna)
    elif lista_comandi[i] == 7:
        visualizzaPavimento(matrice, len(matrice))
    return esegui_comandi(lista_comandi, i + 1, matrice, x, y, penna)



#FUNZIONI PER I COMANDI
def alza_penna(penna):
    penna = False
    return penna

def abassa_penna(penna):
    penna = True
    return penna

def vai_est(matrice, x, y, penna):
    passi = int(input('passi?'))
    print()
    nuova_x = x + passi
    if nuova_x > len(matrice) -1:
        nuova_x = len(matrice) - 1

    if penna:
        for i in range(x + 1, nuova_x + 1):
            matrice[y][i] = 1
    
    return matrice,nuova_x,y

def vai_ovest(matrice, x, y, penna):
    passi = int(input('passi?'))
    print()
    nuova_x = x - passi
    if nuova_x < 0:
        nuova_x = 0
    if penna:
        for i in range(x - 1, nuova_x - 1, -1):
            matrice[y][i] = 1
    return matrice,nuova_x,y

def vai_sud(matrice, x, y, penna):
    passi = int(input('passi?'))
    print()
    nuova_y = y + passi
    if nuova_y > len(matrice) - 1:
        nuova_y = len(matrice) - 1
    if nuova_y < 0:
        nuova_y = 0
    if penna:
        for i in range(y + 1, nuova_y + 1):
            matrice[i][x] = 1
           
    return matrice,x,nuova_y

def vai_nord(matrice, x, y, penna):
    passi = int(input('passi?'))
    print()
    nuova_y = y - passi
    if nuova_y < 0:
        nuova_y = 0
    if penna:
        for i in range(y - 1, nuova_y -1, -1):
            matrice[i][x] = 1
           
    return matrice,x,nuova_y

def visualizzaPavimento(pavimento, dim):
    for i in range(dim):
        for j in range(dim):
            if pavimento[i][j]==1:
                print("*",end="")
            else:
                print(" ",end="")
        print()

def main():
    matrice = init_matrice(20)
    lista_comandi = prendi_comandi()
    matrice = esegui_comandi(lista_comandi, i=0, matrice=matrice, x=0,y=0, penna=True)

main()
    
