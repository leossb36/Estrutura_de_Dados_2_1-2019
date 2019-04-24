import time
import random
import math
from selection import selectionSort
from bubble import bubbleSort
from shell import shellSort
#todo
    # definir random set 
    # definir selection sort
    # definir insertion sort
    # definir bubble sort
    # definir shell sort
values = []
size = int(input('Defina a quantidade de elementos da lista: '))

def getValues(vector, size):
    while len(vector) < size:
        rnd = random.randint(0, size - 1)
        if rnd in vector:
            continue
        else:
            vector += [rnd]
    print("Valores: " + str(vector))

getValues(values, size)

def menu():
    print("---------------------------------------")
    print("                MENU                   ")
    print("---------------------------------------")
    print("1 - Selection Sort")
    print("2 - Bubble Sort")
    print("3 - Shell Sort")
    # print("4 - gera gráfico")
    print("0 - Sair")
    print("---------------------------------------")
    opt = input("Digite uma Opção: ")
    return opt

opt = 0
while opt != '4':
    opt = menu()
    if opt == '1':
        selectionSort(values)
        print(values)
    elif opt == '2':
        bubbleSort(values)
        print(values)
    elif opt == '3':
        shellSort(values)
        print(values)
    # elif opt == '4':
    #     sentinelSearch(vector)
    elif opt == '0':
        print('\n' + 'Obrigado =)' + '\n' + 'Leonardo dos Santos')
        break
    else:
        print('Opção Invalida!')
        break
