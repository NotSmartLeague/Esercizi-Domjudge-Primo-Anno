def trasforma(numero):
    nuovo_numero = ''
    count = 1
    i = 0
    for j in range(i + 1, len(numero)):
        if numero[i] == numero[j]:
            count += 1
        else:
            nuovo_numero += str(count) + numero[i]
            if i + count < len(numero):
                i += count
            else:
                i = len(numero) - 2
            count = 1
    nuovo_numero += str(count) + numero[i]
    return nuovo_numero

def main():
    n = input()
    nuovo_numero = trasforma(n)
    print(nuovo_numero, len(nuovo_numero), end='')
main()