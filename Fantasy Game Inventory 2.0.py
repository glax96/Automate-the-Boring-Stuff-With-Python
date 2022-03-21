from copy import deepcopy

def addToInventory(inventory, addedItems):
    invcopy=deepcopy(inventory)
    for j,k in invcopy.items():
        for i in range(len(addedItems)):
            if addedItems[i]==j:
                inventory[j]=inventory[j]+1
            elif addedItems[i] not in inventory:
                inventory[addedItems[i]]=1
    return inventory

def displayInventory(dic):
    i=0
    j=0
    total=0
    print('Inventory:\n')

    for i, j in dic.items():
        print(str(j) + ' ' + i)
        total=total+j

    print('\nTotal number of items: ' + str(total))

inv = {'ruby': 15, 'gold coin': 42, 'rope': 1, 'dagger': 27}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'rope', 'rope']
inv = addToInventory(inv,dragonLoot)
displayInventory(inv)
