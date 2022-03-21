import sys

def collatz(number):
        if number%2==0:
            print('number//2')
            number=number/2
            return number
        else:
            print('3*number+1')
            number=3*number+1
            return number

while True:
    try:
        print('Upisi broj')
        a=int(input())
        while True:
            a=(collatz(a))
            print(a)
            if a==1:
                break
    except:
        print('You must enter an integer')
        print('Za izlaz upišite q a za nastavak c')
        b=input()
        if b=='q':
            sys.exit()
        else:
            continue
