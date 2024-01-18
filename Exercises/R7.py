def mcd(a,b):
    r = a % b
    if r == 0:
        return b
    return mcd(b,r)

def main():
    a = int(input())
    b = int(input())
    print(mcd(a,b), end='')

main()