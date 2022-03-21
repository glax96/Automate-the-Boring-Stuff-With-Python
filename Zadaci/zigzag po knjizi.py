import time, sys
indent=0#koliko razmaka da odvoji
indentIncreasing=True#jel se razmak povecava ili smanjuje

try:
    while True:#main program loop
        print(' '*indent,end='')
        print('********')
        time.sleep(0.1)#pauza 1/10 sekunde

        if indentIncreasing:
            #povecaj broj razmaka
            indent=indent+1
            if indent==20:
                #promjeni smjer
                indentIncreasing=False

        else:
            #smanji broj razmaka
            indent=indent-1
            if indent==0:
                #promjeni smjer
                indentIncreasing=True
except KeyboardInterrupt:
    sys.exit()
