minimalna_liczba = None
maksymalna_liczba = None


while True:
    liczba = input('Podaj liczbe ')
    if liczba == 'wynik' or not liczba.isdigit():
        break
    wprowadzona_liczba = float(liczba)
    if (maksymalna_liczba is None) or (wprowadzona_liczba > maksymalna_liczba): #kolejność or ma znaczenie - warunek odnoszący się do None musi być na początku
        maksymalna_liczba = wprowadzona_liczba
    if (minimalna_liczba is None) or (wprowadzona_liczba < minimalna_liczba):
        minimalna_liczba = wprowadzona_liczba


if minimalna_liczba is None or maksymalna_liczba is None:
    print('Nie podano liczb')
else:
    print(f'Maksymalna wprowadzona liczba to: {maksymalna_liczba}, a minimalna wprowadzona liczba to: {minimalna_liczba}')
