import sys

def concat_list(l):
    s=''
    i=0
    for word in spam:
        if i==len(spam)-1 and '' not in spam:
            s+='and '
            s+=word
            break
        s+=word
        s+=','
        s+=' '
        i+=1
    return s



spam=[]
while True:
    print('Upisi rijec/broj, q za prestanak upisa')
    spam.append(input())
    if 'q' in spam:
        spam.remove('q')
        break

s=concat_list(spam)
if s=='':
    print('prazna lista')
    sys.exit()
print(s)

