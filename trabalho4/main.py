from heap import heapSort
from radix import lsd_sort
import matplotlib.pyplot as plt
import pandas as pd
import random
import time
import csv

def generateCsv(time):
    filename = 'resultado.csv'
    data = pd.DataFrame(time)
    data.to_csv(filename)

def plotGraph(time):
    pd.DataFrame(time).plot(kind='line')
    titulo = 'Tempo(sec) x Tamanho'
    plt.title(titulo)
    plt.ylabel('Tempo(sec)')
    plt.xlabel('Tamanho')
    plt.show()

def getValues(size):
    arr = []
    while len(arr) < size:
        i = random.randint(0, size - 1)
        if i in arr:
            continue
        else:
            arr += [i]

    return arr

size = int(input('Tamanho do vetor: '))
arr = getValues(size)
print(arr)

timeOrder = {'Heap_Sort': {}, 'Radix_Sort_LSD': {}}
timeOrder['Heap_Sort'].update(timeOrder['Heap_Sort'])
timeOrder['Radix_Sort_LSD'].update(timeOrder['Radix_Sort_LSD'])

for i in range(size):
    start_time = time.time()
    heapSort(arr)
    end_time = time.time()
    delta = end_time - start_time
    timeOrder['Heap_Sort'][i] = delta

for i in range(size):
    start_time = time.time()
    lsd_sort(arr)
    end_time = time.time()
    delta = end_time - start_time
    timeOrder['Radix_Sort_LSD'][i] = delta

generateCsv(timeOrder)
plotGraph(timeOrder)