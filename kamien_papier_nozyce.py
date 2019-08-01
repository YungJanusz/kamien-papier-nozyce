decyzja = True
while decyzja == True:
    gracz1 = input("Kamien, papier czy nożyce???")
    gracz2 = input("Kamien, papier czy nożyce???")
    if gracz1 == gracz2:
        print('REMIS')
    elif gracz1 == 'kamien' and gracz2 == 'papier':
        print('WYGRYWA GRACZ 2')
    elif gracz1 == 'kamien' and gracz2 == 'nozyce':
        print('WYGRYWA GRACZ 1')
    elif gracz1 == 'papier' and gracz2 == 'kamien':
        print('WYGRYWA GRACZ 1')
    elif gracz1 == 'papier' and gracz2 == 'nozyce':
        print('WYGRYWA GRACZ 2')
    elif gracz1 == 'nozyce' and gracz2 == 'kamien':
        print('WYGRYWA GRACZ 2')
    elif gracz1 == 'nozyce' and gracz2 == 'papier':
        print('WYGRYWA GRACZ 1')
    else:
        print('Wprowadz "kamien", "papier" lub "nozyce"!')
    decyzja = input('Chcesz zaczac gre od nowa? Wpisz "tak" lub "nie"')

    if decyzja == 'tak':
        print('Kolejna runda...')
        decyzja = True
    elif decyzja == 'nie':
        print('KONIEC GRY')
        decyzja = False
    else:
        print('Źle, wprowadz "tak" lub "nie"!')

