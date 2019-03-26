liczba = input('Podaj liczbę całkowitą dla której liczysz silnie')
silnia = 1
if liczba.isdigit():
    krok = 1
    liczba = int(liczba)
    while krok <= liczba:
        silnia = krok * silnia
        krok += 1
else:
    print('Wprowadz liczbę')

print(f'Silnia liczby {liczba} = {silnia}')
