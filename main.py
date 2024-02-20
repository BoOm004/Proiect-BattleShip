import random

TABLA_ASCUNSA = [['▢'] * 10 for _ in range(10)]
TABLA_AFISATA = [['▢'] * 10 for _ in range(10)]
LUNGIMEA_NAVELOR = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

transformare_litere = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

def printare_tabla(tabla):
    print('   A B C D E F G H I J')
    for i, rand in enumerate(tabla, 1):
        print(f'{i:2d}', ' '.join(rand))

def verifica_incadrare_nava(lungime_nava, rand, coloana, orientare):
    if orientare == 'O':
        return coloana + lungime_nava <= 10
    else:
        return rand + lungime_nava <= 10

def verifica_suprapunere_nave(tabla, rand, coloana, orientare, lungime_nava):
    if orientare == 'O':
        for i in range(coloana, coloana + lungime_nava):
            if tabla[rand][i] == 'x':
                return True
    else:
        for i in range(rand, rand + lungime_nava):
            if tabla[i][coloana] == 'x':
                return True
    return False

def proximitate_nave(tabla, rand, coloana, lungime_nava, orientare):
    # Trebuie completată această funcție pentru a verifica proximitatea navelor
    for i in range(10):
        for j in range(10):
            if tabla[i][j] == 'y':
                if i > 0 and tabla[i-1][j] in ('y', 'x'):
                    return True
                if i < 9 and tabla[i+1][j] in ('y', 'x'):
                    return True
                if j > 0 and tabla[i][j-1] in ('y', 'x'):
                    return True
                if j < 9 and tabla[i][j+1] in ('y', 'x'):
                    return True
    return False

def amplasare_nava(tabla):
    for lungime_nava in LUNGIMEA_NAVELOR:
        while True:
            orientare = random.choice(['O', 'V'])
            rand = random.randint(0, 9)
            coloana = random.randint(0, 9)
            if verifica_incadrare_nava(lungime_nava, rand, coloana, orientare):
                if not verifica_suprapunere_nave(tabla, rand, coloana, orientare, lungime_nava):
                    if orientare == 'O':
                        for i in range(coloana, coloana + lungime_nava):
                            tabla[rand][i] = 'x'
                    else:
                        for i in range(rand, rand + lungime_nava):
                            tabla[i][coloana] = 'x'
                    break

def introducere_coordonate_nave():
    while True:
        rand = input('Introdu numarul randului: ')
        if rand.isdigit() and 1 <= int(rand) <= 10:
            rand = int(rand) - 1
            break
        else:
            print('Introdu un numar valid între 1 și 10.')

    while True:
        coloana = input('Introdu litera coloanei: ').upper()
        if coloana in transformare_litere:
            coloana = transformare_litere[coloana]
            break
        else:
            print('Introdu o literă validă între A și J.')

    return rand, coloana

def numara_navele_nimerite(tabla):
    return sum(rand.count('x') for rand in tabla)

amplasare_nava(TABLA_ASCUNSA)
print('Să începem jocul.')
print('Ghicește poziția navelor.')

nr_miscari = 100
while nr_miscari > 0:
    printare_tabla(TABLA_AFISATA)
    print('Număr nave scufundate:', numara_navele_nimerite(TABLA_AFISATA))
    rand, coloana = introducere_coordonate_nave()

    if TABLA_AFISATA[rand][coloana] in ('-', 'x'):
        print('Ai încercat deja aici, încearcă alta poziție.')
    elif TABLA_ASCUNSA[rand][coloana] == 'x':
        print('Ai nimerit nava!')
        TABLA_AFISATA[rand][coloana] = 'x'
        nr_miscari -= 1
    else:
        print('Nu ai nimerit nici o nava. Mai încearcă.')
        TABLA_ASCUNSA[rand][coloana] = '-'
        TABLA_AFISATA[rand][coloana] = '-'
        nr_miscari -= 1

    if numara_navele_nimerite(TABLA_ASCUNSA) == 10:
        print('Felicitări! Ai câștigat!')
        break

    print('Au mai rămas', nr_miscari, 'miscări.')

if nr_miscari == 0:
    print('Nu mai ai nicio mișcare disponibilă. Jocul s-a încheiat.')
