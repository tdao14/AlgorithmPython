def selectionSort(a):
    i = 0
    n = len(a)
        while i < n-1:
            s = i
            for j in range(i+1, n):
                 if a[s] > a[j]:
                    s = j
                
            if s != i:
               temp = a[s]
               a[s] = a[i]
               a[i] = temp
                
            i+=1
