def swap(a,b):
    comodo = a
    a = b
    b = comodo

    return a,b


def ottieni_max(stringa):
    for i in range(len(stringa) + 1):
        for j in range(i + 1, len(stringa)):
            if stringa[j] > stringa[i]:
                stringa[j], stringa[i] = swap(stringa[j], stringa[i])
    
    return stringa


def ottieni_min(stringa):
    for i in range(len(stringa) + 1):
        for j in range(i + 1, len(stringa)):
            if stringa[j] < stringa[i]:
                stringa[j], stringa[i] = swap(stringa[j], stringa[i])
    
    return stringa


def lista_stringa(stringa):
    lista = []
    for i in stringa:
        lista.append(i)

    return lista


def lista_int(lista):
    numero = ''
    for i in lista:
        numero += i
    
    return int(numero)

def main():
    numero = input()
    lista = lista_stringa(numero)
    minimo = lista_int(ottieni_min(lista))
    massimo = lista_int(ottieni_max(lista))
    
    print(massimo-minimo, end='')

main()

