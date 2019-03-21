suma = 0
dzien = 1

while dzien <=7:
    liczba = input(f'Podaj kolejną temperaturę dla dnia {dzien}: ')
    suma += float(liczba)
    dzien += 1
print(f'{suma/dzien:.2f}')
