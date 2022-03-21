import sys, time

def zigzag(i):
        print(i*' '+'********')
        time.sleep(0.1)


i=20
j=0
try:
    while True:
        while i>0:
            zigzag(i)
            i=i-1
        print('********')
        while i<20:
            zigzag(i)
            i=i+1
except KeyboardInterrupt:
    sys.exit()



