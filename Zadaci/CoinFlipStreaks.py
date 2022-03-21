import random
numberOfStreaks = 0
hort = []

counterH = 0
counterT = 0
cont = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    hort=[]
    for i in range(100):
        hort.append(random.randint(0,1))

    hort.append('kraj liste')
    # Code that checks if there is a streak of 6 heads or tails in a row.


    for i in hort:
        j = i
        k = i
        for j in hort:
            if j == 0:
                counterH += 1
            if counterH == 6:
                numberOfStreaks += 1
            if cont == 6:
                break
            if j=='kraj liste':
                break
            cont += 1
        cont=0
        for k in hort:
            if k == 1:
                counterT += 1
            if counterT == 6:
                numberOfStreaks += 1
            if cont == 6:
                break
            if k=='kraj liste':
                break
            cont += 1
        cont=0
        counterH = 0
        counterT = 0

print('Chance of streak: %s%%' % (numberOfStreaks / (100*10000)))
