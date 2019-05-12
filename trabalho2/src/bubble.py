import time

def bubbleSort(vector):
    start_time = time.time()
    for i in range(len(vector)):
        for j in range(0, len(vector) - i - 1):
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
    elapsed_time = time.time() - start_time #converting to seconds
    print('tempo gasto: ' + str(round(elapsed_time, 4)) + ' sec')
