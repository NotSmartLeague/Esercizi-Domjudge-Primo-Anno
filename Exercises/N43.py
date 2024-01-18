def parentisizzata(espressione):
    aperte = 0
    chiuse = 0

    for i in espressione:
        if i == '(':
            aperte += 1
        elif i == ')':
            chiuse += 1
        
        if chiuse > aperte:
            return False
    
    return chiuse == aperte

def superflue(espressione):
    for i in range(len(espressione) - 1):
        j = i + 1
        if espressione[i] == '(' and espressione[j] == ')':
            return False
    return True

def main():
    espressione = input()
    if parentisizzata(espressione):
        print("ok1")
    else:
        print("no1")
    if superflue(espressione):
        print("ok2")
    else:
        print("no2")

main()

# (c+(-(a+))-d)