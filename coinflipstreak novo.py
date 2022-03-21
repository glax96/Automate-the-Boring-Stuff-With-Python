import random
numberOfStreaks = 0
hort=[]
streak=0
i=0
j=0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    hort=[]
    i=0
    for i in range(100):
        hort.append(random.randint(0,1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for j in hort:
        if j==0:
            pass
        elif hort[j]==hort[j-1]:
            streak+=1
        else:
            streak=0
        if streak==6:
            numberOfStreaks+=1

    j=0
    streak=0
print('Chance of streak: %s%%' % (numberOfStreaks / (100*10000)))
