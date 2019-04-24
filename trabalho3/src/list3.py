from timeit import default_timer as timer
import matplotlib.pyplot as plt
import random
import os.path
from sort import quickSort
from sort import shellSort
from sort import bucketSort

def getValues(vector, size):
    while len(vector) < size:
        rnd = random.randint(0, size - 1)
        if rnd in vector:
            continue
        else:
            vector += [rnd]

def writeData(vector, size):
    getValues(vector, size)
    
    if(os.path.isfile('values.txt')):
        file = open('values.txt', 'r')
        file.close()

    file = open("values.txt", 'a')
    file.write("%s\n" %str(vector))
    file.close()

data = []
size = int(input('Defina a quantidade de elementos da lista: '))

writeData(data, size)
start_time = timer()
print('------------------------------------\n')
print('\tQuick sort\t')
print('------------------------------------\n')
print('Antes de ordenado: ')
print(data)
print('------------------------------------\n')
print('Depois de ordenado: ')
quickSort(data, 0, size - 1)
print(data)
end_time = timer()
quicktime = (end_time - start_time)*3.6*100
print('------------------------------------\n')
print('Tempo = %f sec\n' % quicktime)

random.shuffle(data)

start_time = timer()
print('------------------------------------\n')
print('\tshell sort\t')
print('------------------------------------\n')
print('Antes de ordenado: ')
print(data)
print('------------------------------------\n')
print('Depois de ordenado: ')
s = shellSort(data)
print(s)
end_time = timer()
shelltime = (end_time - start_time)*3.6*100
print('------------------------------------\n')
print('Tempo = %f sec\n' % shelltime)

random.shuffle(data)

start_time = timer()
b = bucketSort(data)
print('------------------------------------\n')
print('\tBucket sort\t')
print('------------------------------------\n')
print('Antes de ordenado: ')
print(data)
print('------------------------------------\n')
print('Depois de ordenado: ')
print(b)
end_time = timer()
buckettime = (end_time - start_time)*3.6*100
print('------------------------------------\n')
print('Tempo = %f sec\n' % buckettime)

plt.title("Type Sort x Time")
plt.xlabel('Type Sort')
plt.ylabel('Time')
x = range(3)

timeall = [quicktime, shelltime, buckettime]
colors=["red", "green", "blue"]
plt.bar(x, timeall, color = colors)
plt.xticks(x, ('Quicksort', 'ShellSort', 'BucketSort'))
plt.grid(linewidth=.1)
plt.show()