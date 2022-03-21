dict =  {'2a':'bpawn', '2b': 'bpawn', '2c':'bpawn', '2d': 'bpawn', '2e': 'bpawn',\
         '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',\
         '1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bqueen', \
         '1e':'bking', '1f': 'brook', '1g': 'bknight', '1h': 'bbishop', \
         '3a': 'bpawn', '7b': 'wking', '7c': 'wqueen'}
chessx = ['a','b','c','d','e','f','g','h']
chessy = ['1','2','3','4','5','6','7','8']

width=8
height=8
chess_positions=[]

def isValidChessBoard(dic):
    x=0
    y=0
    bpiece=0
    wpiece=0
    bking=0
    wking=0
    wpawn=0
    bpawn=0
    wknight=0
    bknight=0
    brook=0
    wrook=0
    wbishop=0
    bbishop=0
    wqueen=0
    bqueen=0

    #Provjera figurica
    for i in dic.values():
        first_char = i[0]
        if first_char == 'w':
            wpiece += 1
        elif first_char == 'b':
            bpiece += 1

        if wpiece<16 and bpiece<16:
            continue
        else:
            return False

    #Provjera kralja
    for v in dic.values():

        if v == 'bking':
            bking+=1
        if bking>1:
            return False
        if v == 'wking':
            wking+=1
        if wking>1:
            print('wking')
            return False
    if wking == 0 or bking == 0:
        return False

        #Provjera pijuna
        if v == 'wpawn':
            wpawn+=1
        if wpawn>7:
            return False
        if v == 'bpawn':
            bpawn+=1
        if bpawn>7:
            return False

        #provjera topova
        if v == 'wrook':
            wrook+=1
        if wrook>2:
            return False
        if v == 'brook':
            brook+=1
        if brook>2:
            return False

        #Provjera konja
        if v == 'wknight':
            wknight+=1
        if wknight>2:
            return False
        if v == 'bknight':
            bknight+=1
        if bknight>2:
            return False

        #Provjera lovca
        if v == 'wbishop':
            wbishop+=1
        if wbishop>2:
            return False
        if v == 'bbishop':
            bbishop+=1
        if bbishop>2:
            return False

        #Provjera kraljice
        if v == 'wqueen':
            wqueen+=1
        if wqueen>2:
            return False
        if v == 'bqueen':
            bqueen+=1
        if bqueen>2:
            return False

    #for za ispisivanje sahovskih pozicija
    for x in range(width):
        for y in range(height):
            chess_positions.append(chessy[y]+chessx[x])

    #Provjera pozicije
    for j in dict.keys():
        if j not in chess_positions:
            return False
        else:
            continue

    return True



if isValidChessBoard(dict) is True:
    print('There is no bug found in game')
else:
    print('There is a bug in game')
