def prendi_risposte():
    lista_risposte_totali = []
    risposta_studente = []
    for i in range(90):
        matricola = input()
        risposte = input()
        risposta_studente.append(matricola)
        risposta_studente.append(risposte)
        lista_risposte_totali.append(risposta_studente)
        risposta_studente = []
    return lista_risposte_totali

def contolla(risposte_esatte, lista_risposte_totali):
    lista_risultati_totali = []
    punteggio = 0
    for i in range(len(lista_risposte_totali)):
        for j in range(20):
            if lista_risposte_totali[i][1][j] != 'X':
                if lista_risposte_totali[i][1][j] == risposte_esatte[j]:
                    #print(lista_risposte_totali[i][1][j], '==', risposte_esatte[j])
                    punteggio += 2
                    #print(punteggio)
                else:
                    #print(lista_risposte_totali[i][1][j], '!=', risposte_esatte[j])
                    punteggio -= 1
                    #print(punteggio)
        lista_risultati_totali.append([lista_risposte_totali[i][0], punteggio])
        #(lista_risposte_totali[i][0], punteggio)
        punteggio = 0
    return lista_risultati_totali

def main():
    risposte_esatte = input()
    risposte_studenti = prendi_risposte()
    risultati_test = contolla(risposte_esatte, risposte_studenti)
    for studente in risultati_test:
        print(studente[0],studente[1])

main()
