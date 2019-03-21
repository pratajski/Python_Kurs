# warzywa = ['marchew', 'kalafior', 'pietruszka']
# for warzywo in warzywa:
#     print(warzywo)

liczby = [-3, -2, 1, -4, 6, 8, 9]
dodatnie = 0
ujemne = 0

for liczba in liczby:
    if liczba < 0:
        ujemne += 1
    else:
        dodatnie += 1

print(f'Ilosc liczby dodatnich = {dodatnie}, a ujemnych = {ujemne}')

