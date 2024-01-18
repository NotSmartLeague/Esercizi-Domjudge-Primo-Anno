def verifica(stringa):
    if stringa[0] in '0123456789':
        return False
    for i in stringa:
        if i.isnumeric() or i.isalpha() or i == '_':
            pass
        else:
            return False
    return True


def main():
    stringa = input()
    if verifica(stringa):
        print('SI', end='')
    else:
        print('NO', end='')

main()
