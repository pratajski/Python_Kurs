from random import randint
import math
skarb_x = randint(1, 10)
skarb_y = randint(1, 10)
gracz_x = randint(1, 10)
gracz_y = randint(1, 10)
odleglosc_x = math.fabs(skarb_x - gracz_x)
odleglosc_y = math.fabs(skarb_y - gracz_y)
minimalna_ilosc_krokow = odleglosc_x + odleglosc_y
reset = 0
liczba_ruchow = 0

print(f'Stoisz na polu x = {gracz_x}, y = {gracz_y}. Możliwe kierunki to:')
print('Góra = w')
print('Dół = s')
print('Prawo = a')
print('Lewo = d')

while True:
    #print(f'Skarb jest na pozycji x = {skarb_x} i y = {skarb_y}')

    kierunek_ruchu = input('Ruszasz się w kierunku ')
    kierunek_ruchu = kierunek_ruchu.lower()
    liczba_ruchow += 1
    reset += 1
    if kierunek_ruchu == 'w':
        gracz_y += 1
    elif kierunek_ruchu == 's':
        gracz_y -= 1
    elif kierunek_ruchu == 'a':
        gracz_x -= 1
    elif kierunek_ruchu == 'd':
        gracz_x += 1
    print(f'Twoja nowa pozycja to {gracz_x}, {gracz_y}')
    if (gracz_x <= 0) or (gracz_x > 10) or (gracz_y > 10) or (gracz_y <= 0):
        print('Postać wyszła poza planszę')
        break
    if math.fabs(skarb_x - gracz_x) > odleglosc_x or math.fabs(skarb_y - gracz_y) > odleglosc_y:
        if randint(0, 4) != 4:
            print('Oddalasz sie od skarbu')
        odleglosc_x = math.fabs(skarb_x - gracz_x)
        odleglosc_y = math.fabs(skarb_y - gracz_y)
    else:
        odleglosc_x = math.fabs(skarb_x - gracz_x)
        odleglosc_y = math.fabs(skarb_y - gracz_y)
        if randint(0, 4) != 4:
            print('Zbliżasz się do skarbu')
    if gracz_x == skarb_x and gracz_y == skarb_y:
        print(f'Znalazleś skarb w {liczba_ruchow} ruchach')
        break
    if reset >= 2 * minimalna_ilosc_krokow:
        skarb_x = randint(1, 10)
        skarb_y = randint(1, 10)
        reset = 0
        print('Skarb zmienił położenie')

