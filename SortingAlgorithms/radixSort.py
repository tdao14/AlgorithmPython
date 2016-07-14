# This radix sort only work if all the number in the list have the same size
# Ex : alist = [340,320,143,525,234,525,132,252,242,252,142,243,525,243]

def radixSort(alist):
    
    size = len(alist)
    alist1 = [0] * size
    divNum = 1
    firstList = True
        
        
    numSizeCheck = alist[0]
        
    while numSizeCheck // divNum != 0:
            
        numberOfElement = 0
        digit = 0
        while numberOfElement < size:

            i = 0
            while i < size and numberOfElement < size:

                if firstList:
                    number = (alist[i] // divNum) % 10
                    if number == digit:
                        alist1[numberOfElement] = alist[i]
                        numberOfElement += 1
                else:
                    number = (alist1[i] // divNum) % 10
                    if number == digit:
                        alist[numberOfElement] = alist1[i]
                        numberOfElement += 1
                                
                                
                i += 1
                        
            digit += 1
                
        divNum *= 10
        firstList = not firstList
        
    if not firstList:
        for i in range(size):
            alist[i] = alist1[i]