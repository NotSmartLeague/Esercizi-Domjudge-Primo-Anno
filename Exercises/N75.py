def cerca_lettera(lettera, frase):
    for i in frase:
        if i == lettera:
            return True
    return False

def controlla(frase):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    flag = False
    for lettera in alfabeto:
        if lettera.isalpha():
            if cerca_lettera(lettera, frase):
                flag = True
            else:
                return False
    return flag

def main():
    frase = input()
    if controlla(frase):
        print('SI', end='')
    else:
        print('NO', end='')

main()