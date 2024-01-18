def prendi_lista():
    lista = []
    elemento = input()
    while elemento != ':':
        lista.append(elemento)
        elemento = input()
    lista.append(':')
    return lista

def nome_valido(stringa):
    if stringa[0].isalpha():
        for j in range(1, len(stringa)):
            if stringa[j].lower() in 'abcdefghijklmnopqrstuvwxyz0123456789' or stringa[j] == '_':
                pass
            else:
                return False
    else:
        return False
    return True

def controlla(lista):
    #si controlla che il primo elemento sia 'def' e l'ultimo ':'
    if lista[0] != 'def' or lista[-1] != ':':
        return False
    #si controlla che il primo carattere del secondo elemento, ovvero il nome della funzione,sia una lettera
    if lista[1][0].isalpha():
        pass
    else:
        return False
    #si controlla che il nome della funzione contenga solo caratteri alfanumerici o _
    for i in range(1, len(lista[1])):
        if lista[1][i].isalnum() or lista[1][i] == '_':
            pass
        else:
            return False
    #si controlla che il terzo elemento sia una parentesi tonda aperta
    if lista[2] == '(':
        pass
    else:
        return False
    #si controlla la validità dei parametri con un ciclo while fin quando non si incontra la parentesi chiusa
    virgola_valida = False
    i = 3
    while lista[i] != ')':
        if virgola_valida:
            if lista[i] == ',':
                virgola_valida = False
            else:
                return False
        else:
            if lista[i] == ',':
                return False
            else:
                #si controlla se i parametri contengono caratteri non validi
                if nome_valido(lista[i]):
                    #print('STEP 5 FATTO')
                    virgola_valida = True
                else:
                    return False
        i += 1
    
    if lista[i + 1] == ':':
        return True
    else:
        return False

def main():
    lista = prendi_lista()
    if len(lista) > 4:
        if controlla(lista):
            print('SI', end='')
        else:
            print('NO', end='')
    else:
        print('NO', end='')

main()