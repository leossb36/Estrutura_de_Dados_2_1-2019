def countingSort(arr, exp1): 
	size = len(arr) 
	output = [0] * (size) 
	count = [0] * (10) 

	for i in range(0, size): 
		index = (arr[i]//exp1) 
		count[ (index)%10 ] += 1

	for i in range(1,10): 
		count[i] += count[i-1] 

	i = size-1
	while i>=0: 
		index = (arr[i]//exp1) 
		output[ count[ (index)%10 ] - 1] = arr[i] 
		count[ (index)%10 ] -= 1
		i -= 1

	i = 0
	for i in range(0,len(arr)): 
		arr[i] = output[i] 

def lsd_sort(arr): 
	max1 = max(arr) 
	exp = 1

	while max1/exp > 0: 
		countingSort(arr,exp) 
		exp *= 10
