# Proiect-BattleShip
Un joc are:
- un id unic
- 2 table (10 x 10) (pentru fiecare jucator)
- 2 jucatori


Fiecare jucator are pe tabla urmatoare nave:
- 1x 4 casute
- 2x 3 casute
- 3x 2 casute
- 4x 1 casuta


Conditii de castig:
- unul dintre jucatori pierde toate navele
- celalalt castiga


Defasurarea jocului:
- Incepe un jucator la intamplare
- La fiecare tura:
    - Jucatorul alege o casuta de a inamicului (fara a ii vedea navele)

    - In cazul in care inamicul are nava in casuta aleasa:
        - Se marcheaza ca distrusa
   
    - Daca inamicul nu mai are nave:
        - Jucatorul curent castiga
   
    - Daca jucatorul curent a ghicit corect casuta inamicului:
        - Jucatorul curent mai joaca inca o tura

    - Daca jucatorul curent nu a ghicit casuta inamicului:
        - Incepe tura inamicului
   
Generare tabla de joc:

- Generam navele in ordinea descrescatoare a dimensiunilor
    - Mai intai generam nava ce ocupa 4 casute
    - Apoi generam navele de 3 casute
    - etc.

- Fiecare nava poate fi pozitionata pe orizontala sau pe verticala

La fiecare pas de generare:
    - incercam o orientare aleatoare (random verticala/orizontala)
    - construim o lista cu pozitii valide pentru nava
    - folosim o functie ce ne spune daca pe pozitia (l, c) putem pune in matrice o nava de dimensiunea s orientata vertical sau orizontal dupa caz
        ```python
        def pozitie_valida(matrice, linie, coloana, dimensiune, orientare):
            if pozitii_libere(...) and pozitii_libere_imprejur(..):
                lista_pozitii_valide.append( (linie, coloana) )
        ```
    - alegem din lista_pozitii_valide o pozitie aleatoare cu random.choice(lista_pozitii_valide)
    - plasam nava pe pozitia aleasa (marcam in matrice)
