import datetime
rok_urodzenia = int(input('Podaj rok urodzenia: '))
# aktualna_data = datetime.datetime.now()
# aktualny_rok = aktualna_data.year
aktualny_rok = datetime.datetime.now().year


if aktualny_rok-rok_urodzenia >= 18:
    print('Jesteś pelnoletni')
else:
    print('Nie jesteś pelnoletni')
