tappo = '*'
bol = False
N=input()

while N!=tappo:
    if N in "aeiou":
        bol = True
    N=input()

    

if bol==True:
    print("ALMENO 1 VOCALE", end='')
elif bol==False:
    print("NESSUNA VOCALE", end='')

    

    