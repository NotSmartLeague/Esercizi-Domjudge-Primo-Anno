def codifica(stringa):
    nuova_stringa = ''
    for i in range(len(stringa)):
        if stringa[i] in 'aeiou':
            nuova_stringa += stringa[i] + 'f' + stringa[i]
        else:
            nuova_stringa += stringa[i]
    return nuova_stringa

def stampa_meta_invertita(stringa):
    for i in range(len(stringa) // 2, len(stringa)):
        print(stringa[i], end='')
    for i in range(0,len(stringa) // 2):
        print(stringa[i], end='')

def main():
    stringa = input()
    nuova_stringa = codifica(stringa)
    stampa_meta_invertita(nuova_stringa)

main()