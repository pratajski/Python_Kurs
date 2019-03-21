# zbior = set(range(1, 10))
# zbior2 = set(range(1, 10, 3))
# nieparzyste = set(range(1, 20, 2))
# # print(nieparzyste)
# ulubione = set(range(3,9))
# suma = ulubione | nieparzyste
# print(suma)
# iloczyn = ulubione & nieparzyste
# print(iloczyn)
# xor = nieparzyste ^ ulubione
# print(xor)

zbior = set()
while True:
    liczba = input('Proszę podaj liczbę ')

    if liczba == '':
        break

    zbior.add(int(liczba)) # zapewnia unikatowosc liczb

parzyste = set(range(0, 101, 2))

print(f'Parzystych liczb od 0 do 100 jest {len(zbior & parzyste)}')