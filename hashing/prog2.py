#User function Template for python3

#Complete this function
def QuadraticProbing( hash, hashSize, arr, sizeOfArray):
    counter = 0
    for i in range(0,sizeOfArray):
        hashval = arr[i]%hashSize
        if (hash[hashval]==-1):
            hash[hashval] = arr[i]
            counter += 1
        else:
            val = hash[hashval]
            m = 0
            while(hash[hashval]!=-1) & (counter != hashSize):
                m = m+1
                res = (arr[i]%hashSize) + m*m
                hashval = res%hashSize
            if counter != hashSize:
                hash[hashval] = arr[i]
                counter += 1



#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    
    while(T>0):
        
        
        hashSize=int(input())
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        hash=[-1]*hashSize
        
        QuadraticProbing( hash, hashSize, arr, sizeOfArray)
        
        for i in hash:
            print(i,end=" ")
        print()
        T-=1


if __name__=="__main__":
    main()
# } Driver Code Ends
