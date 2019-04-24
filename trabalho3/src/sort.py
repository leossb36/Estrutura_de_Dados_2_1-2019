
def partition(arr,low,high): 
    pivot = arr[high] 
    i = low - 1
    for j in range(low , high): 
        if(arr[j] <= pivot): 
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i + 1],arr[high] = arr[high],arr[i + 1] 
  
    return (i+1) 
def quickSort(arr,low,high): 
    if low < high:
        ptt = partition(arr,low,high)
        quickSort(arr, low, ptt - 1)
        quickSort(arr, ptt + 1, high)

def shellSort(arr): 
    n = len(arr) 
    gap = n//2
   
    while gap > 0: 
        for i in range(gap,n): 
            temp = arr[i] 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
            arr[j] = temp 
        gap //= 2

    return arr
    
def bucketSort(arr):
    high = max(arr)
    length = len(arr)
    size = high/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(arr[i]/size)
        if j != length:
            buckets[j].append(arr[i])
        else:
            buckets[length - 1].append(arr[i])
 
    for i in range(length):
        insertionSort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while (j >= 0 and temp < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp