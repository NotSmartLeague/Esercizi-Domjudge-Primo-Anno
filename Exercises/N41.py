posti = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

count_non_fumatori = 0
count_fumatori = 0
while count_fumatori + count_non_fumatori < 10:
    posto = int(input("Digitare 1 per fumatori o 2 per non fumatori:"))
    if posto == 1:
        for x in range(0,5):
            if posti[x] == 0:
                posti[x] = 1
                print("Reparto fumatori, posto", x + 1)
                count_fumatori += 1
                break
            if count_fumatori == 5:
                scelta = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?") 
                if scelta == 'S':
                    for x in range(5,10):
                        if posti[x] == 0:
                            posti[x] = 1
                            print("Reparto NON fumatori, posto", x + 1)
                            count_non_fumatori += 1
                            break
                    break
                else:
                    print("Il prossimo volo parte tra 3 ore")
                    break

    elif posto == 2:
        for x in range(5,10):
            if posti[x] == 0:
                posti[x] = 1
                print("Reparto NON fumatori, posto", x + 1)
                count_non_fumatori += 1
                break
            if count_non_fumatori == 5:
                scelta = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?") 
                if scelta == 'S':
                    for x in range(0,5):
                        if posti[x] == 0:
                            posti[x] = 1
                            print("Reparto fumatori, posto", x + 1)
                            count_fumatori += 1
                            break
                    break
                else:
                    print("Il prossimo volo parte tra 3 ore")
                    break

    