def controlla(sequenza):
    andamento = 'crescente'
    if sequenza[0] >= sequenza[1]:
        return False
    for i in range(len(sequenza) - 1):
        if andamento == 'crescente':
            if sequenza[i] == sequenza[i + 1]:
                return False
            elif sequenza[i] > sequenza[i + 1]:
                andamento = 'decrescente'
        else:
            if sequenza[i] <= sequenza[i + 1]:
                return False
    if andamento == 'decrescente':
        return True
    return False    

def prendi_sequenza():
    sequenza = []
    n = int(input())
    while n != 0:
        sequenza.append(n)
        n = int(input())
    return sequenza


def main():
    sequenza = prendi_sequenza()
    if len(sequenza) > 2:
        if controlla(sequenza):
            print('SI', end='')
        else:
            print('NO', end='')
    else:
        print('NO', end='')

if __name__ == '__main__':
    main()