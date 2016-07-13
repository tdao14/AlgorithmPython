def bubbleSort(a):
    n = len(a)
        swapped = True
        i = 0
        while i < n-1 and swapped:
            swapped = False
                for j in range(n-i-1):
                    if a[j] > a[j+1]:
                        temp = a[j]
                            a[j] = a[j+1]
                                a[j+1] = temp
                                swapped = True
                i+=1 
