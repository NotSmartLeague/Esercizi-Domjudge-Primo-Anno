def romboidale1(n, x, totale):
    if x == 1:
        return totale + 1
    totale += x * 2 - 1
    return romboidale1(n, x - 1, totale)

def romboidale2(x,totale):
    if x == 1:
        return totale + 1
    totale += x * 2 - 1
    return romboidale2(x - 1, totale )
    


def main():
    n = int(input())
    if n == 1:
        print(n, end='')
    else:
        print(romboidale1(n, n, 0) + romboidale2(n - 1,0), end='') 

main()