napis = 'Ala ma <kota>, a kot ma Alę'
napis = napis.lower()
indeks_poczatek = None
indeks_koniec = None

for indeks, litera in enumerate (napis):
    if litera == '<':
        indeks_poczatek = indeks
    if litera == '>':
        indeks_koniec = indeks
        break

print('Pomiędzy nawiasami jest', indeks_koniec - indeks_poczatek - 1, 'znaków')
