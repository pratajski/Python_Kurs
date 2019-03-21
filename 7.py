liczba = float(input('Podaj liczbę: '))
jest_parzysta = liczba % 2 == 0
podzielna_przez_3 = liczba % 3 == 0
wieksza_niz_10 = liczba > 10

# print((not jest_parzysta and podzielna_przez_3 and wieksza_niz_10) or liczba == 7)
print('Liczba jest nieparzysta, podzielna przez 3 i większa od 10 lub = 7:', (not jest_parzysta and podzielna_przez_3 and wieksza_niz_10) or liczba == 7)
# print('Liczba jest nieparzysta, podzielna przez 3 i większa od 10 lub = 7:', ((liczba%2 != 0) and (liczba%3==0) and (liczba>10)) or (liczba == 7))