pozycja_x = int(input('Podaj pozycję gracza X: '))
pozycja_y = int(input('Podaj pozycję gracza Y: '))

# pozycja_x = 50
# pozycja_y = 50

if pozycja_x < 0 or pozycja_y < 0 or pozycja_x > 100 or pozycja_y > 100:
    print('Jesteś poza planszą')
#elif pozycja_x >= 40 and pozycja_x <= 60 and pozycja_y >= 40 and pozycja_y <= 60: w wersji skróconej poniżej
elif 40 <= pozycja_x >= 60 and 40 <= pozycja_y >= 60:
    print('Jesteś w środku')
else:
    if pozycja_x <= 50:
        print('Jesteś w lewej ', end='')
    else:
        print('Jesteś w prawej ', end='')
    if pozycja_y <= 50:
        print('dolnej ćwiartce')
    else:
        print('górnej ćwiartce')
