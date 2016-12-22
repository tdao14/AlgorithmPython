    def mergeSort(a): #pass as a reference or it won’t work
    
        #split
        aSize = len(a)
        if aSize > 1:
            mid = aSize // 2
            rightArray = a[mid:]
            leftArray = a[:mid]
                
            mergeSort(rightArray)
            mergeSort(leftArray)
                
            r = 0
            l = 0
            rightArrayLen = len(rightArray)
            leftArrayLen = len(leftArray)
                
            i = 0
                
            while r < rightArrayLen and l < leftArrayLen:
                if rightArray[r] < leftArray[l]:
                    a[i] = rightArray[r]
                    r += 1
                else:
                    a[i] = leftArray[l]
                    l +=1
                i+=1
            
            while r < rightArrayLen:
                a[i] = rightArray[r]
                r +=1
                i +=1
                
                
            while l < leftArrayLen:
                a[i] = leftArray[l]
                l += 1
                i += 1
