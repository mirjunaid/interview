def bubleSort(items):
    change = 0
    for i in range(len(items)):
        for j in range(len(items), i- 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                change += change + 1


    print(items)

print('Welcome to the buble sort algorithm')
number = input('Enter the list items seperated by spaces: ')
items = number.split().replace(' ' by ',')
bubleSort(items)
