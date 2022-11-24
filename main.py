from random import randint

tabla = []
for x in range(10):
    tabla.append(['#'] * 10) 

def printare_tabla(tabla):    
    coloana = ('A B C D E F G H I J')
    rand = ('0 1 2 3 4 5 6 7 8 9')
    nr_rand = 0
    print(' ' * 3, coloana)
    print()
    for rand in tabla:        
        print(nr_rand,' ', (' ').join(rand))
        nr_rand += 1

def creare_nave (tabla):
    for nava in range(10):
        nava_rand, nava_coloana = randint(0,10), randint(0,10)
        while tabla[nava_rand][nava_coloana] == 'X': # 'X' pentru navele pe care le-am nimerit
            nava_rand, nava_coloana = randint(0,10), randint(0,10)
        tabla[nava_rand][nava_coloana] = 'X'   


def pozitie_nava(tabla, nava, pozitie, orientare, x, y):
    rand = input('Introdu numarul randului: ').upper()
    while rand not in '0123456789':
        print('Introdu un numar valid ex: 0,1,2,3,4,5,6,7,8,9')
        rand = input('Introdu numarul randului: ').upper()
    
    coloana = input('Introdu litera coloanei: ').upper()
    while coloana not in 'ABCDEFGHIJ':
        print('Introdu o litera valida ex: A,B,C,D,E,F,G,H,I,J')
        coloana = input('Introdu litera coloanei: ').upper()

    orientare = input('Introdu v/o pentru tipul orientarii; ').upper()
    while orientare not in 'VO':
        print('Introdu o orientare valida ex: V - verticala, O - orizontala')
        orientare = input('Introdu v/o pentru tipul orientarii; ').upper()

    V = 'veritcal'
    O = 'orizontal'
     # x este pentru orientarea pe verticala
    if orientare == V:
        for i in range(nava):
            tabla[x][y+1] = pozitie
    # y este pentru orientare pe orizonala
    elif orientare == O:
        for i in range(nava):
            tabla[y][x+1] = pozitie
    return int(rand) - 1, coloana

def numara_navele_nimerite (tabla):
    numaratoare = 0
    for rand in tabla:
        for coloana in rand:
            if coloana == 'X':
                numaratoare += 1
    return numaratoare

if __name__ == '__main__':
    creare_nave(tabla)
    print('Ghiceste ppozitia navelor')
    print(tabla)
    rand, coloana  =pozitie_nava()
    # '-' cand nu ai nimerit nava/ si casuta a fost deja aleasa
    if tabla [rand] [coloana] == '-': 
        print('Ai incercat deja aici, vezi alta pozitie.')
    elif tabla [rand] [coloana] == 'X':
        print('Ai nimerit nava')
        tabla [rand] [colona] = 'X'
        
    else:
        print('Nu ai nimeri nava, mai incearca.')
        tabla [rand] [coloana] = '-'
    if numara_navele_nimerite(tabla) == 10:
        print('Felicitari!!! Ai castigat razboiul!!!')
print("   Let's start Battleship")
printare_tabla(tabla)