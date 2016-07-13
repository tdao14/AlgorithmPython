def insertionSort(a):
	n = len(a)
	for i in range(n-1):
		swapped = True
		j = i + 1
		while j >= 1 and swapped:
			if a[j] < a[j-1]:
				temp = a[j]
				a[j] = a[j-1]
				a[j-1] = temp
				j-=1
			else:
				swapped = False

