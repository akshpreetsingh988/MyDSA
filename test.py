# implementing quadratic hashing 

def quadratic_hashing(arr , m) : 
    hashTable = [-1] * m 
    for x in arr: 
        index = x%m 
        i=0 
        if hashTable[index] ==-1: 
            hashTable[index]=x 
        else: 
            i=0 
            while True: 
                pos = (index + i*i) %m
                if hashTable[pos]==-1: 
                    hashTable[pos] = x
                    break  
                elif hashTable[pos]==x: 
                    break 
                i+=1 
                if i==m: 
                    break 
        
    print(hashTable) 
if __name__== "__main__" : 
    arr=  [31 , 48 , 37, 70] 

    hashSize = 4
    quadratic_hashing(arr, hashSize) 
