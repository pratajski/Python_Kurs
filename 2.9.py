produkty = {
    'piwo': 3.5,
    'woda': 2,
    'fanta': 3.5,
    'wódka': 50,
    'wino': 20
}

print('Nazwy produktów i ceny za sztukę:')
# for nazwa in produkty:
#     print(nazwa, produkty[nazwa])

while True:
    for nazwa, cena in produkty.items():
        print(nazwa, '\t', cena)


    # towar = 'woda'
    towar = input('Wpisz nazwę towaru jaki chcesz zakupić ')

    if towar not in produkty:
        print('Nie mamy tego w sklepie')
    else:
        ilosc = float(input('Wpisz ilość towaru jaką chcesz zakupić '))
        print('Wartość zamówienia wynosi ', produkty[towar.lower()]*ilosc)
        break
