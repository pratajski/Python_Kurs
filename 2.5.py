# kolumna_wartosc = []

# print('\t', 0, '\t', 1, '\t', 2, '\t', 3, '\t', 4, '\t', 5, '\t', 6, '\t', 7, '\t', 8, '\t', 9)
print('\t\t', end='')
for poczatek in range (0, 10):

    print(poczatek, end='\t')
print('\n')
for wiersz in range(0, 10):
    print(wiersz, end= '\t\t')
    for kolumna in range(0, 10):
        # kolumna_wartosc.append(wiersz * kolumna)
        print(wiersz * kolumna, end= '\t')
    print()
