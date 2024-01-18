def prendi_input():
    s = input()
    n = int(input())
    elenco = []
    for i in range(n):
        elenco.append(input())

    return s, elenco

def trova_massimo_minimo(elenco):
    massimo = elenco[0]
    for i in elenco:
        if i > massimo:
            massimo = i
    minimo = elenco[0]
    for i in elenco:
        if i < minimo:
            minimo = i
    return massimo + minimo

def verifica(s, elenco):
    for i in range(len(elenco)):
        for j in range(len(elenco)):
            #print(elenco[i] + elenco[j])
            if elenco[i] + elenco[j] == s:
                return 'OK'
    return trova_massimo_minimo(elenco)

def main():
    s, elenco = prendi_input()
    print(verifica(s, elenco), end='')

main()
    