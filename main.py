import random
from random import randint

TABLA_ASCUNSA = [['▢'] * 10 for i in range(10)]
TABLA_AFISATA = [['▢'] * 10 for i in range(10)]
LUNGIMEA_NAVELOR = [1,1,1,1,2,2,2,3,3,4]

def printare_tabla(tabla):    
    coloana = ('A B C D E F G H I J')
    rand = ('0 1 2 3 4 5 6 7 8 9')
    nr_rand = 0
    print(' ' * 3, coloana)
    print()
    for rand in tabla:        
        print(nr_rand,' ', (' ').join(rand))
        nr_rand += 1

transformare_litere = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

#verifica incadrare nava pe tabla
def verifica_incadrare_nava(LUNGIME_NAVA, rand, coloana, orientare):
    #verifica orientarea pe orizontala
    if orientare == 'O':
        if coloana + LUNGIME_NAVA > 10:
            return False
        else:
            return True
    #verifica orientarea pe verticala
    else:
        if rand + LUNGIME_NAVA > 10:
            return False
        else:
            return True

def verifica_suprapunere_nave(tabla, rand, coloana, orientare, lungime_nava):
    # verificare in cazul pozitionarii pe orizontala
    if orientare == 'O':
        for i in range(coloana, coloana + lungime_nava):
            if tabla[rand][i] == 'x':
                return True
    # verificare in cazul pozitionarii pe verticala            
    else:
        for i in range (rand, rand + lungime_nava):
            if tabla[i][coloana] == 'x':
                return True     
    return False

def amplasare_nava(tabla):
    for lungime_nava in LUNGIMEA_NAVELOR:
        while True:
            orientare = random.choice(['O', 'V'])
            rand = randint (0, 9)
            coloana = randint (0, 9)
            if verifica_incadrare_nava(lungime_nava, rand, coloana, orientare):
                if verifica_suprapunere_nave(tabla, rand, coloana, orientare, lungime_nava) == False:
                    if orientare == 'O':
                        for i in range (coloana, coloana + lungime_nava):
                            tabla[rand][i] = 'x'
                    else:
                        for i in range (rand, rand + lungime_nava):
                            tabla[i][coloana] = 'x'
                    break        
    
def introducere_coordonate_nave ():
    if introducere_coordonate_nave == True:
        while True:
            try:
                rand = input('Introdu numarul randului: ')
                if rand in '0123456789':
                    rand = int(rand) - 1
                    break
            except ValueError:
                print('Introdu un numar valid ex: 0,1,2,3,4,5,6,7,8,9')
        while True:
            try:
                coloana = input('Introdu litera coloanei: ').upper()
                if coloana in 'ABCDEFGHIJ':
                    coloana = transformare_litere[coloana]
                    break
            except KeyError:
                print('Introdu o litera valida ex: A,B,C,D,E,F,G,H,I,J')
        while True:
            try:
                orientare = input('Introdu orientarea O/V : ').upper()
                if orientare == 'O' or orientare == 'V':
                    break
            except TypeError:
                print('Introdu V/O pentru tipul orientarii: ')
        return rand, coloana, orientare
    else:
        while True:
            try:
                rand = input('Introdu numarul randului: ')
                if rand in '0123456789':
                    rand = int(rand) - 1
                    break
            except ValueError:
                print('Introdu un numar valid ex: 0,1,2,3,4,5,6,7,8,9')
        while True:
            try:
                coloana = input('Introdu litera coloanei: ').upper()
                if coloana in 'ABCDEFGHIJ':
                    coloana = transformare_litere[coloana]
                    break
            except KeyError:
                print('Introdu o litera valida ex: A,B,C,D,E,F,G,H,I,J')  
        return rand, coloana

def numara_navele_nimerite(tabla):
    numaratoare = 0
    for rand in tabla:
        for coloana in rand:
            if coloana == 'x':
                numaratoare += 1
    return numaratoare

amplasare_nava(TABLA_ASCUNSA)
printare_tabla(TABLA_AFISATA)
print('Numar nave scufundate: ', numara_navele_nimerite(TABLA_AFISATA))
print('Sa incepem jocul.')
nr_miscari = 100
while nr_miscari > 0:
    print("Ghiceste pozitia navelor.")
    rand, coloana = introducere_coordonate_nave()
    if TABLA_AFISATA[rand][coloana] == '-':
        print('Ai incercat deja aici, vezi alta pozitie.')
    elif TABLA_ASCUNSA[rand][coloana] =='x':
        print('Ai nimerit nava')
        TABLA_AFISATA[rand][coloana] = 'x'
        nr_miscari -= 1
    else:
        print('Nu ai nimerit nici o nava. Mai incearca.')
        TABLA_ASCUNSA[rand][coloana] ='-'
        nr_miscari -= 1
    if numara_navele_nimerite(TABLA_ASCUNSA) == 10:
        print('Felicitari ai castigat!!!')
        break
    print("Au mai ramas " + str(nr_miscari) + 'miscari')
    if nr_miscari == 0:
        print("Nu mai ai nici o miscare")