import time

def heapify_desc(arr, n, i):
	smallest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and arr[i] > arr[l]:
		smallest = l

	if r < n and arr[smallest] > arr[r]:
		smallest = r


	if smallest != i:
		arr[i],arr[smallest] = arr[smallest],arr[i]
		heapify_desc(arr, n, smallest)
		global swaps_counter
		swaps_counter += 1

def heapSort_desc(arr):
	n = len(arr)

	for i in range(n // 2 - 1, -1, -1):
		heapify_desc(arr, n, i)

	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify_desc(arr, i, 0)

arr = [ 12, 11, 13, 5, 6, 7]
swaps_counter = 0
start_time = time.time()
heapSort_desc(arr)
print ("Sorted array is")
print(arr)
print("Swaps number is")
print(swaps_counter)
end_time = time.time()
print("Time spent:")
print(end_time-start_time)