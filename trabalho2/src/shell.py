import time

def shellSort(vector):
    start_time = time.time()
    size = len(vector)
    gap = size/2

    while gap > 0:
        for i in range(gap, size):
            aux = vector[i]
            j = i

            while j >= gap and vector[j-gap] > aux:
                vector[j] = vector[j-gap]
                j = j - gap

            vector[j] = gap
        gap = int(gap // 2)

    elapsed_time = time.time() - start_time #converting to seconds
    print('tempo gasto: ' + str(round(elapsed_time, 4)) + ' sec')