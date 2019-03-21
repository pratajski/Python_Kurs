miasto_a = input('Podaj nazwę pierwszego miasta ')
miasto_b = input('Podaj nazwę drugiego miasta ')
dystans = float(input(f'podaj dystans pomiedzy {miasto_a}, a miastem {miasto_b} '))
cena_paliwa = float(input('Podaj cenę paliwa '))
spalanie = float(input('Podaj średnie spalanie na 100km '))
# koszt_przejazdu = (spalanie / 100) * cena * dystans

#print(f'Cena przejazdu na trasiae {miasto_a} - {miasto_b} = {dystans * cena_paliwa * (spalanie / 100)}')

#zaokrąglenie - :.0f obcina miejska dziesiętne do ilości cyfry pomiedzy . a f
print(f'Cena przejazdu na trasiae {miasto_a} - {miasto_b} = {dystans * cena_paliwa * (spalanie / 100):.0f}')