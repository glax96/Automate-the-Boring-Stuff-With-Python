import random
import sys

win=0
loss=0
tie=0
print('We are playing rock, paper, scissors!')
print('')
print(str(win)+' Wins,' +str(loss)+ ' Losses,'+str(tie)+' Ties')
#print('1st one to get to 5 wins, wins the battle')

while True:
    print('Enter your move: r(ock) (p)aper (s)cissors or (q)uit')
    player1=input()
    pc=random.choice('rps')
    if player1=='q':
        print('You left the game')
        sys.exit()
    elif player1=='r':
        print('ROCK versus...')
    elif player1=='p':
        print('PAPER versus...')
    elif player1=='s':
        print('SCISSORS versus...')

    if pc=='r':
        print('ROCK')
    elif pc=='p':
        print('PAPER')
    elif pc=='s':
        print('SCISSORS')

    if player1==pc:
        print('It is a tie!')
        tie=tie+1
        print(str(win)+' Wins,' +str(loss)+ ' Losses,'+str(tie)+' Ties')
    elif player1=='r' and pc=='s' or player1=='p' and pc=='r' or player1=='s' and pc=='p':
        print('You Win!')
        win=win+1
        print(str(win)+' Wins,' +str(loss)+ ' Losses,'+str(tie)+' Ties')
    elif player1=='s' and pc=='r' or player1=='r' and pc=='p' or player1=='p' and pc=='s':
        print('You lost!')
        loss=loss+1
        print(str(win)+' Wins,' +str(loss)+ ' Losses,'+str(tie)+' Ties')
