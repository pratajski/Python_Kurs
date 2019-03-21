napis = 'Ala ma <kota>, a kot <ma> Alę'
slownik = {}

for litera in napis.lower():
    if litera not in slownik:
        slownik[litera] = 0
    slownik[litera] += 1
for litera, liczba in slownik.items():
    print(f'Znak {litera} wystąpił: {liczba} razy')