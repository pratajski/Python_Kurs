print('Obliczmy ciag fibonnaciego', '\n', 'test')
ciag = [1]
liczba = input('Podaj ilość liczb ciągu fibbonaciego chcesz wypisać = ')
if liczba.isdigit():
    liczba = int(liczba)
    if liczba < 1:
        print('Podaj liczba naturalną większą od 0')
    else:
        krok = 1
        temp_liczba = 0
        while krok <= liczba:
            ciag.append((ciag[krok-1])+temp_liczba)
            temp_liczba = ciag[krok - 1]
            krok += 1
        print(f'Ciąg fibonacciego liczby {liczba } wynosi {ciag}')
else:
    print('Podaj liczba naturalną większą od 0')
