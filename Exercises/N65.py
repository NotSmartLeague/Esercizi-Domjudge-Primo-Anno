def input_pesi():
    pesi = []
    for _ in range(8):
        pesi.append(int(input()))
    return pesi

def prendi_voti(): #funzione che ritorna una matrice, in cui ogni elemento è una lista formata dallo studente con i rispettivi voti
    voti = []
    studente = [] #si gestisce lo studente come una lista, in cui l'elemento 0 è la matricola e il resto sono i voti
    for _ in range(70):
        studente.append(input())
        for _ in range(8):
            studente.append(int(input()))
        voti.append(studente)
        studente = []
    return voti

def calcola_voti(voti, pesi):
    lista_voti = [] 
    voto_finale_studente = [] #si gestisce il voto finale come una lista che ha al posto 0 la matricola, e al posto 1 il voto collegato
    voto_studente = 0
    for studente in voti: #si itera nella lista dei voti presi in precedenza
        for j in range(1,9):
            voto_studente += studente[j] * pesi[j - 1] #si calcola il voto per singolo studente
        voto_finale_studente.append(studente[0]) #si aggiunge la matricola dello studente al voto finale
        voto_finale_studente.append(voto_studente)
        lista_voti.append(voto_finale_studente)
        voto_finale_studente = []
        voto_studente = 0
    return lista_voti #ritorna una matrice in cui l'elemento 0 è la matricola e l'elemento 1 il voto calcolato

def stampa_studente(studente):
    print(studente[0],studente[1])

def promuovi(lista_voti, soglia): #funzione che aggiunge in una nuova lista tutti gli alunni con voto maggiore alla soglia
    promossi = []
    for i in lista_voti:
        if i[1] >= soglia:
            promossi.append(i)
    return promossi

def trova_max(promossi):
    massimo = promossi[0]
    for i in promossi:
        if i[1] > massimo[1]:
            massimo = i
    return massimo

def trova_min(promossi):
    minimo = promossi[0]
    for i in promossi:
        if i[1] < minimo[1]:
            minimo = i
    return minimo

def main():
    pesi = input_pesi()
    voti = prendi_voti()
    lista_risultati = calcola_voti(voti, pesi)
    soglia = int(input())
    promossi = promuovi(lista_risultati, soglia)
    massimo = trova_max(promossi)
    minimo = trova_min(promossi)
    for i in promossi:
        stampa_studente(i)
    print(len(promossi), end=' ')
    print(massimo[0], end=' ')
    print(minimo[0], end='')
    


main()




