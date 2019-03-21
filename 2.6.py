lista = [1, 5, -1, -2, 10, 15, 22]

maksimum_indeks = None
minimum_indeks = None

for indeks, wartosc in enumerate(lista):
    if minimum_indeks is None or lista[minimum_indeks] > wartosc:
        minimum_indeks = indeks
    if maksimum_indeks is None or lista[maksimum_indeks] < wartosc:
        maksimum_indeks = indeks
    # if min is None:
    #     if lista[liczba] > max:
    #         max = lista[liczba]
    #     if lista[liczba] < min:
    #         min = lista[liczba]

if minimum_indeks is not None and maksimum_indeks is not None:
    # liczba_max_temp = lista[minimum_indeks]
    # lista[minimum_indeks] = lista[maksimum_indeks]
    # lista[maksimum_indeks] = liczba_max_temp
    # jest równoznaczne z 
    lista[minimum_indeks], lista[maksimum_indeks] = lista[maksimum_indeks], lista[minimum_indeks]

print('max = ', maksimum_indeks, lista[maksimum_indeks])
print('min = ', minimum_indeks, lista[minimum_indeks])

print(lista)
