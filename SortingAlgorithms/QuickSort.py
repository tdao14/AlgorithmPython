def partition(a, first, last):
    left = first + 1
    right = last
    pivotValue = a[first]
        
    done = False
        
    while not done:
            
        while left <= right and a[left] <= pivotValue :
            left += 1
                
            while left <= right and a[right] >= pivotValue:
                right -= 1
                
            if left <= right:
                temp = a[left]
                a[left] = a[right]
                a[right] = temp
            else:
                done = True


    temp = a[first]
    a[first] = a[right]
    a[right] = temp
        
    return right

def quickSort(a):
    quickSortHelper(a, 0, len(a)-1)


def quickSortHelper(a, first, last):
    if first < last:
        splitPoint = partition(a, first , last)
            
            quickSortHelper(a, first, splitPoint-1)
                quickSortHelper(a, splitPoint+1, last)
