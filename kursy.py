euro = 4.2
usd = 3.54
chf = 3.58
pl = 1

print("Tabela wymiany walut na złotówki", '\n', 'Możesz wybrać następujące waluty', '\n', "EURO, USD, CHF")
operacja = input("Wybierz K dla kupna i S dla sprzedaży ").lower()

if operacja == 'k':
    wybor = input('podaj walutę jaką chcesz kupić ').lower()
    ilosc = input('Ile złotówek chcesz wymienić? ')
    if ilosc.isdigit():
        ilosc = float(ilosc)
        if wybor == 'euro':
            print(f'Otrzymasz {ilosc / euro} Euro')
        elif wybor == 'usd':
            print(f'Otrzymasz {ilosc / usd} USD')
        elif wybor == 'chf':
            print(f'Otrzymasz {ilosc / chf} CHF')
        else:
            print('Podałeś złą walutę')
    else:
        print('Nie podałeś liczby')
elif operacja == 's':
    wybor = input('podaj walutę jaką chcesz sprzedać ').lower()
    ilosc = input('Ile waluty chcesz wymienić? ')
    if ilosc.isdigit():
        ilosc = float(ilosc)
        if wybor == 'euro':
            print(f'Otrzymasz {euro * ilosc} zł')
        elif wybor == 'usd':
            print(f'Otrzymasz {usd * ilosc} zł')
        elif wybor == 'chf':
            print(f'Otrzymasz {chf * ilosc} zł')
        else:
            print('Podałeś złą walutę')
    else:
        print('Nie podałeś liczby')
else:
    print('Zły kod operacji')
