szerokosc_opakowania = float(input('Podaj szerokość opakowania w cm '))
dlugosc_opakowania = float(input('Podaj długość opakowania w cm '))
wysokosc_opakowania = float(input('Podaj wysokosc opakowania w cm '))

objetosc_opakowania = szerokosc_opakowania * dlugosc_opakowania * wysokosc_opakowania

print(f'Objetosc wynosi {objetosc_opakowania}')
print(f'Objętość jest większa od 1 litra?  {objetosc_opakowania > 1000}')

# if objetosc_opakowania > 1000:
#     print('Opakowanie ma pojemność większą niż 1l')
# elif objetosc_opakowania == 1000:
#     print('Opakowanie ma pojemność 1l')
# else:
#     print('Opakowanie ma pojemność mniejszą niż 1l')