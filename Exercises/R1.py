def sequenza(n):
    if n == 0:
        return 2
    return 3 * (n + 1) * sequenza(n - 1)

def main():
    n = int(input())
    print(sequenza(n), end='')

main()