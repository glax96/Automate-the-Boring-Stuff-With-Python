def displayInventory(dic):
    i=0
    j=0
    total=0
    print('Inventory:\n')

    for i, j in dic.items():
        print(str(j) + ' ' + i)
        total=total+j

    print('\nTotal number of items: ' + str(total))

dict={}
dio=''
for i in range(100):
    print('Write name of the item:\n(enter q to exit inserting)')
    keys = input()
    dio=keys
    if 'q' in dio:
        break
    print('Write quantity of the item:')
    values = int(input())
    dict[keys] = values

displayInventory(dict)



