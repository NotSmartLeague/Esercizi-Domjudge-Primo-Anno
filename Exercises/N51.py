def verifica(stringa1, stringa2):
    for i in stringa1:
        if i in stringa2:
            return i
    return 'DISGIUNTE'

def prendi_stringa():
    stringa = ''
    while True:
        char = input()
        if char == '.':
            break
        stringa += char

    return stringa

def main():
    stringa1 = prendi_stringa()
    stringa2 = prendi_stringa()
    print(verifica(stringa1, stringa2), end='')


main()  