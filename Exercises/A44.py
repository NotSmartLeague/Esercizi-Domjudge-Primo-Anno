def lista_codice(codice):
    lista = []

    for i in codice:
        lista.append(int(i))
    
    #print('il codice è diventato la lista:', lista)
    return lista

def verifica(lista):
    somma1 = 0
    somma2 = 0
    for i in range(0, len(lista) // 2):
        somma1 += lista[i]

    for i in range((len(lista) // 2), len(lista)):
        somma2 += lista[i]
    # print('somma1:', somma1)
    # print('somma2:', somma2)
    return somma1 == somma2

def main():
    codice = input()
    lista = lista_codice(codice)
    if not codice:
        print('SFORTUNATO')
    else:
        if verifica(lista):
            print('FORTUNATO', end='')
        else:
            print('SFORTUNATO', end='')

main()
