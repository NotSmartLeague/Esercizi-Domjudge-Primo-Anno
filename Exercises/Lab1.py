def prendi_sequenze():
    seq1 = []
    seq2 = []
    n = int(input())
    #sequenza 1
    for _ in range(n):
        seq1.append(int(input()))
    #sequenza 2
    for _ in range(n):
        seq2.append(int(input()))
    
    return seq1, seq2

def antireciproco(a, b, c, d):
    return (a * c) / (b * d) == -1


def controlla(seq1, seq2):
    cont = 0
    for i in range(len(seq1) - 1):
        if cont == 2:
            # print(cont, '<--cont')
            break
        if antireciproco(seq1[i], seq2[i], seq1[i +1], seq2[i + 1]):
            # print(seq1[i] ,'/', seq2[i])
            # print(seq1[i + 1] ,'/', seq2[i + 1])
            cont += 2
        else:
            # print(seq1[i] ,'/', seq2[i])
            # print(seq1[i + 1] ,'/', seq2[i + 1])
            cont = 0
    return cont == 2

def main():
    seq1, seq2 = prendi_sequenze()
    # print(controlla(seq1, seq2))
    if controlla(seq1, seq2):
        print('SI', end='')
    else:
        print('NO', end='')

main()
