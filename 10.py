pierwsza_liczba = float(input('Podaj pierwszą liczbę: '))
druga_liczba = float(input('Podaj drugą liczbę: '))

# pierwsza_liczba = 2
# druga_liczba = 3
dzialanie = input('Wpisz znak działania ')

if dzialanie == '+':
    print('Wynik = ', pierwsza_liczba + druga_liczba)
elif dzialanie == '*':
    print('Wynik = ', pierwsza_liczba * druga_liczba)
elif dzialanie == '/':
    if druga_liczba == 0:
        print('Nie dzielimy przez 0')
    else:
        print('Wynik = ', pierwsza_liczba / druga_liczba)

elif dzialanie == '-':
    print('Wynik = ', pierwsza_liczba - druga_liczba)
elif dzialanie == '^':
    print('Wynik = ', pierwsza_liczba**druga_liczba)
else:
    print('Wprowadzono nieobsługiwany znak działania')