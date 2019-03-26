podstawa = input('Podaj podstawę potęgowania ')
wykladnik = input('Podaj wykładnik ')
wynik = 1

if podstawa.isdigit() and wykladnik.isdigit():
    podstawa = int(podstawa)
    wykladnik = int(wykladnik)

    krok = 1

    while krok <= wykladnik:
        wynik = podstawa * wynik
        krok += 1
    print(f'wynik = {wynik}')

else:
    print('wykładnik i podstawa musza byc liczbami całkowitymi większymi od 0')
