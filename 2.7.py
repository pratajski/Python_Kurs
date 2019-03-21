# napis = 'Ala ma kota i psa'
napis = input('wpisz zdanie ')
# napis = napis.lower()
samogloski = 'aeiou'
ilosc_samoglosek = 0
#'w' in samogloski

for litera in napis.lower():
    if litera in samogloski:
        ilosc_samoglosek += 1
print(ilosc_samoglosek)



# print(napis)