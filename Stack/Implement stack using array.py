# You need to write code for push() and pop()

class MyStack:
    
    def __init__(self):
        self.arr=[]
        self.top = -1
    
    #Adds element to the Stack
    def push(self,data):
        self.top += 1
        try:
            self.arr[self.top] = data
        except:
            (self.arr).append(data)
        return self.arr
    
    #Removes element from the stack
    def pop(self):
        if (self.top==-1):
            return -1
        m = self.top
        self.top -= 1
        return self.arr[m]
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyStack()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
# } Driver Code Ends
