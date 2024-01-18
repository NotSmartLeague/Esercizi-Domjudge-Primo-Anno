def prendi_a():
    A = []
    for i in range(26):
        #print(i,'. ', end='', sep='')
        char = input()
        A.append(char)
    
    return A


def prendi_b():
    B = []
    N = int(input())
    for i in range(N):
        #print(i,'. ', end='', sep='')
        elemento = int(input())
        B.append(elemento)
    
    return B


def stampa_parola(A, B):
    parola = ''
    for i in (B):
        if i < 26:
            parola += A[i]

    return parola


def main():
    A = prendi_a()
    B = prendi_b()

    print(stampa_parola(A,B), end='')


main()