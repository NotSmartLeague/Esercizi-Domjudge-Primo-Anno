def prendi_lista():
    lista = []
    n = int(input())
    for i in range(n):
        elemento = int(input())
        lista.append(elemento)
    return lista

def reverse(lista,i, reversed_list):
    if i == 0:
        reversed_list.append(lista[0])
        return reversed_list
    reversed_list.append(lista[i])
    return reverse(lista, i - 1, reversed_list)

def main():
    lista = prendi_lista()
    reversed_list = reverse(lista, len(lista) - 1, [])
    for i in reversed_list:
        print(i, end='')

main()