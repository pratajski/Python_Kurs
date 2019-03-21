napis = 'Ala ma <kota>, a kot <ma> Alę'
napis = napis.lower()

czy_zliczac = False
liczba_znakow = 0

for litera in napis:
    if litera == '>':
        # break # liczy pierwszy nawias
        czy_zliczac = False # liczy przy większej ilości nawiasów
    elif czy_zliczac:
        liczba_znakow += 1
    if litera == '<':
        czy_zliczac = True

print('Pomiędzy nawiasami jest', liczba_znakow, 'znaków')
