def swap(a,b):
    comodo = a
    a = b
    b = comodo

    return a,b


def input_sequenza_principale():
    sequenza = []
    while True:
        n = int(input())
        if n < 0:
            break
        sequenza.append(n)
    
    return sequenza

def cerca_sottosequenze(sequenza):
    if sequenza:
        matrice = []
        sottosequenza = []
        for i in range(0, len(sequenza) - 1):
            #print(sottosequenza)
            j = i + 1
            if sequenza[i] <= sequenza[j]:
                #print(sequenza[i], '<=', sequenza[j])
                sottosequenza.append(sequenza[i])
            else:
                #print(sequenza[i], '>', sequenza[j])
                sottosequenza.append(sequenza[i])
                #print('aggiungiamo', sequenza[i],'alla sottosequenza', sottosequenza)
                if len(sottosequenza) > 1:
                    matrice.append(sottosequenza)
                    #print('aggiungiamo la sottosequenza', sottosequenza,'alla matrice', matrice)
                sottosequenza = []
                #print('puliamo la sottosequenza per riutilizzarla', sottosequenza)
        
        if sequenza[-1] >= sequenza[-2]:
            sottosequenza.append(sequenza[-1])
        matrice.append(sottosequenza)
        #print('aggiungiamo la sottosequenza', sottosequenza,'alla matrice', matrice)
        #print(sequenza)
    return matrice

def ottieni_risultato(matrice):
    for i in range(len(matrice) + 1):
        for j in range(i + 1, len(matrice)):
            if len(matrice[i]) < len(matrice[j]):
                matrice[i], matrice[j] = swap(matrice[i], matrice[j])
    # print(matrice)
    risultato = [matrice[0], len(matrice[0])]
    return risultato


def controlla_len_1(matrice):
    for i in matrice:
        if len(i) > 1:
            return False
        return True

def stampa_max(matrice):
    for i in range(len(matrice) + 1):
        for j in range(i + 1, len(matrice)):
            if matrice[i] < matrice[j]:
                matrice[i], matrice[j] = swap(matrice[i], matrice[j])
    return matrice

def stampa_risultato(lista):
    if lista[0]:
        for i in lista[0]:
            print(i,end='')
        print('\n',lista[1], end='', sep='')
    else:
        print('Empty', end='')

def main():
    sequenza_principale = input_sequenza_principale()
    if not sequenza_principale:
        print('Empty', end='')
    else:
        matrice_sottosequenza = cerca_sottosequenze(sequenza_principale)
        #print(matrice_sottosequenza)
        if not matrice_sottosequenza[0]:
            print(sequenza_principale[0])
            print(1,end='')
        else:
            risultato = ottieni_risultato(matrice_sottosequenza)
            stampa_risultato(risultato)


main()