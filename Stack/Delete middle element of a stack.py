#User function Template for python3

##Complete this function
def deleteMid(s, sizeOfStack, current):
    if current==sizeOfStack//2:
        s.pop()
        return s
    t=s[-1]
    s.pop()
    s=deleteMid(s,sizeOfStack,current+1)
    s.append(t)
    return s



#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():
    testcases=int(input())
    while(testcases>0):
        
        sizeOfStack=int(input())
        
        myStack=[int(x) for x in input().strip().split()]
        
        if(sizeOfStack==1):
            print(myStack[0])
        else:
            modified=deleteMid(myStack,sizeOfStack,0)
            
            while(len(modified)>0):
                print(modified[-1],end=" ")
                modified.pop()
            print()
        
        testcases-=1


if __name__=="__main__":
    main()
    
    
# } Driver Code Ends
