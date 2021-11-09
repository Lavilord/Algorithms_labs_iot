import time

def heapify_asc(arr, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and arr[i] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r


	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i]
		heapify_asc(arr, n, largest)
		global swaps_counter
		swaps_counter += 1



def heapSort_asc(arr):
	n = len(arr)

	for i in range(n // 2 - 1, -1, -1):
		heapify_asc(arr, n, i)

	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify_asc(arr, i, 0)


arr = [ 12, 11, 13, 5, 6, 7]
swaps_counter = 0
start_time = time.time()
heapSort_asc(arr)
print ("Sorted array is")
print(arr)
print("Swaps number is")
print(swaps_counter)
end_time = time.time()
print("Time spent:")
print(end_time-start_time)

