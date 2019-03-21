liczba = []

while len(liczba) < 10:
    wartosc = input('Podaj wartość ')
    # if wartosc == '':
    #     break
    # if wartosc.isdigit():
    #     liczba.append(float(wartosc))
    #     suma = sum(liczba)
    #     srednia = suma / len(liczba)
    # else:
    #     break

    if wartosc == '':
        break
    elif not wartosc.isdigit():
        print('To nie jest liczba')
    else:
        liczba.append(int(wartosc))
if len(liczba) == 0:
    print('Nie wpisano liczb')
else:
    # suma = sum(liczba)
    # srednia = suma / len(liczba)
    print('Średnia = ', sum(liczba) / len(liczba))


