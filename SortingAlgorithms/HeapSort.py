def heapSort(a):
    n = len(a)
        
        for i in range(n,-1,-1):
            heapSortHelper(a,i)
        
        while n > 0:
            temp = a[n-1]
                a[n-1] = a[0]
                a[0] = temp
                n-=1
                
                print(a.pop())
                heapSortHelper(a,0)

def	heapSortHelper(a, parent):
    x = heapDown(a,parent)
        while(x != -1):
            x = heapDown(a,x)


def heapDown(a, parent):
    
    leftChild = parent * 2 + 1
        rightChild = parent * 2 + 2
        largest = -1
        
        
        if leftChild < len(a):
            if rightChild < len(a) and a[rightChild] > a[leftChild]:
                largest = rightChild
                else:
                    largest = leftChild
                
                if a[largest] > a[parent]:
                    temp = a[largest]
                        a[largest] = a[parent]
                        a[parent] = temp
    
    return largest
