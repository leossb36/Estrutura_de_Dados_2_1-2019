def heapFy(arr, size, index):
    largest = index # raiz
    left = 2*index+1
    right = 2*index+2

    if left < size-1 and arr[index] < arr[left]:
        largest = left # atualiza raiz
    
    if right < size-1 and arr[index] < arr[right]:
        largest = right # atualiza raiz

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index] # faz swap
        heapFy(arr, size, largest) # chamada recursiva

def heapSort(arr):
    size = len(arr)
    
    for i in range(size, -1, -1): # build heap
        heapFy(arr, size, i)
    
    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapFy(arr, i, 0)

    return arr