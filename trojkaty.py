# Przygotuj program, który odbierze trzy boki trójkąta i zwróci informację, czy trójkąt jest prostokątny, równoramienny, rozwartokątny.
# Pamiętaj o obsłużeniu sytuacji gdy na podstawie długości boków nie będzie można stworzyć trójkąta.
# Podaj długość pierwszego boku: 2 Podaj długość drugiego boku: 3 Podaj długość trzeciego boku: 5 Figura o podanych bokach nie jest trójkątem

bok_A = input('Podaj długość boku A ')
bok_B = input('Podaj długość boku B ')
bok_C = input('Podaj długość boku C ')
print()
najdluzszy = 0

if bok_A.isdigit() and bok_B.isdigit() and bok_C.isdigit():
    bok_A = int(bok_A)
    bok_B = int(bok_B)
    bok_C = int(bok_C)
    najdluzszy = bok_A
    if bok_B > najdluzszy:
        najdluzszy = bok_B
    if bok_C > najdluzszy:
        najdluzszy = bok_C
    if najdluzszy < (bok_A + bok_B + bok_C - najdluzszy):
        if bok_A == bok_B or bok_A == bok_C or bok_B == bok_C:
            print('Trójkąt jest równoramienny')
        if bok_A == najdluzszy:
            if bok_A * bok_A > bok_B * bok_B + bok_C * bok_C:
                print('Trójkąt jest rozwartokatny')
            elif bok_A * bok_A == bok_B * bok_B + bok_C * bok_C:
                print('Trójkąt jest prostokątny')
            else:
                print('Trójkąt jest ostrokątny')
        if bok_B == najdluzszy:
            if bok_B * bok_B > bok_A * bok_A + bok_C * bok_C:
                print('Trójkąt jest rozwartokatny')
            elif bok_B * bok_B == bok_A * bok_A + bok_C * bok_C:
                print('Trójkąt jest prostokątny')
            else:
                print('Trójkąt jest ostrokątny')
        if bok_C == najdluzszy:
            if bok_C * bok_C > bok_B * bok_B + bok_A * bok_A:
                print('Trójkąt jest rozwartokatny')
            elif bok_C * bok_C == bok_B * bok_B + bok_A * bok_A:
                print('Trójkąt jest prostokątny')
            else:
                print('Trójkąt jest ostrokątny')
    else:
        print('Figura o podanych bokach nie jest trójkątem')
else:
    print('długość boków musi być liczbą')
