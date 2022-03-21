import random

i=0
b=0
a=random.randint(0,20)
print('I am thinking of a number between 1 and 20')
print('Take a guess.')
b=int(input())
while a!=b:

    if b>a:
        print('Your guess is too high.')
    elif b<a:
        print('Your guess is too low.')
    print('Take a guess.')
    b=int(input())
    i=i+1
print('Good job! You guessed my number in ' + str(i) + ' guesses!')
