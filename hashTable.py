class hashTable:
    # I initilize the list with -1
    # -2 is key that deleted
    def __init__(self):
        self.__size = 11;
        self.__numberOfElement = 0
        self.__key = [-1] * self.__size
        self.__value = [-1] * self.__size
    
    def getSize(self):
        return self.__size
    
    def getNumberOfElement(self):
        return self.__numberOfElement
    
    def insert(self, key, value):
        if type(key) == int:
            if self.__numberOfElement == self.__size:
                self.__rehash()
            
            i = 1
            index = self.__hashFunction(key)
            while self.__key[index] != -2 and self.__key[index] != -1:
                if i > (self.__size // 2):
                    self.__rehash()
                    index = self.__hashFunction(key)
                    i = 1
                
                index = (index + i * i) % self.__size
                i += 1
            
            self.__key[index] = key
            self.__value[index] = value
            self.__numberOfElement += 1
        
        else:
            print('Key must be an integer')

    def searchKey(self, key):
        index = self.__search(k)
        if index != -1:
            return self.__value[index]
        else:
            print("We can't found the index that match the key that you provided")


    def delete(self, key):
        index = self.__search(k)
        if index != -1:
            self.__key[index] = -2
            self.__value[index] = -2
        else:
            print("We can't found the index that match the key that you provided")




    def printList(self):
        for i in range(self.__size):
            print(self.__key[i], self.__value[i])



    def __getitem__(self, k):
        self.search(key)

    def __setitem__(self, k, value):
        index = self.__search(k)
        if index != -1:
            self.__value[index] = value
        else:
            print("We can't found the index that match the key that you provided")



    def __rehash(self):
    
        nextPrime = self.__size * 2 + 1
        
        while (not self.__isprime(nextPrime)):
            nextPrime += 2

        # copy the list of key and value into a temp list
        tempKeyList = self.__key
        tempValueList = self.__value
        tempSize = self.__size
        # set a value for size = nextPrime
        self.__size = nextPrime
        
        # create a new list for the __key and __value
        self.__key = [-1] * self.__size
        self.__value = [-1] * self.__size
        
        i = 0
        
        while i < tempSize:
            if tempKeyList[i] != -1 and tempKeyList[i] != -2:
                self.insert(tempKeyList[i], tempValueList[i])
            i += 1

    def __hashFunction(self, number):  # quadratic hashing
        return number % self.__size
    
    def __isprime(self, n):
        
        if n == 2 or n == 3:
            return True
        
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        i = 5
        x = 2
        
        while i * i <= n:
            if n % i == 0:
                return False
            
            i += x
            x = 6 - x
        
        return True
    
    def __search(self, key):
        
        i = 1
        index = self.__hashFunction(key)
        found = False
        limit = self.__size // 2 + 1
        result = -1
        
        while not found and i < limit:
            if self.__key[index] == key:
                result = index
                found = True
            elif self__key[index] == -1:
                found = True
            else:
                index = (index + i * i) % self.__size
                i += 1

        return result


