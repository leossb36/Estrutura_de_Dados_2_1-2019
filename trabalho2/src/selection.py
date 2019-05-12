import time

def selectionSort(vector):
    start_time = time.time()
    for i in range(len(vector)):
        iMin = i
        for j in range(i+1, len(vector)):   
            if(vector[iMin] > vector[j]):
                iMin = j
        vector[i], vector[iMin] = vector[iMin], vector[i]
    elapsed_time = time.time() - start_time #converting to seconds
    print('tempo gasto: ' + str(round(elapsed_time, 4)) + ' sec')
