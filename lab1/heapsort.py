import time

swaps_counter = 0
comparisons_counter = 0

def heapify(arr, n, i, order):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2
	global swaps_counter
	global comparisons_counter
	if order == "asc":
		comparisons_counter+=1
		if l < n and arr[i] < arr[l]:
			largest = l

		comparisons_counter += 1
		if r < n and arr[largest] < arr[r]:
			largest = r

		comparisons_counter += 1
	elif order == "desc":
		comparisons_counter += 1
		if l < n and arr[i] > arr[l]:
			largest = l

		comparisons_counter += 1
		if r < n and arr[largest] > arr[r]:
			largest = r

		comparisons_counter += 1

	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i]
		heapify(arr, n, largest, order)
		swaps_counter += 1


def heapsort(arr, order):
	n = len(arr)

	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i, order)

	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0, order)


if __name__ == '__main__':
	arr = [ 12, 11, 13, 5, 6, 7]
	start_time = time.time()
	order = "desc"
	heapsort(arr,order)
	print ("Sorted array is", arr)
	print("Swaps number is",swaps_counter)
	end_time = time.time()
	print("Time spent:", end_time-start_time)
	print("Number of comparisons:",comparisons_counter)

