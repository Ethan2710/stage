mot = input('écris un mot')
e = mot.count("e")
if e == 0:
    print('Il n y a pas de "e" dans ce mot')
if e == 1:
    print('Il y a un "e" dans ce mot')
if e > 1:
    print('Il y a des "e" dans ce mot') 