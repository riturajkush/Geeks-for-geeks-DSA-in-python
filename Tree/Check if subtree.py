#User function Template for python3




'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should print the left view of the binary tree
# Note: You aren't required to print a new line after every test case

def isSubTree(T, S): 
      
    # Base Case 
    if S is None: 
        return True
  
    if T is None: 
        return False
  
    # Check the tree with root as current node 
    if (areIdentical(T, S)): 
        return True
  
    # IF the tree with root as current node doesn't match 
    # then try left and right subtreee one by one 
    return isSubTree(T.left, S) or isSubTree(T.right, S)
    
def areIdentical(root1, root2): 
      
    # Base Case 
    if root1 is None and root2 is None: 
        return True
    if root1 is None or root2 is None: 
        return False
  
    # Check fi the data of both roots is same and data of 
    # left and right subtrees are also same 
    return (root1.data == root2.data and 
            areIdentical(root1.left , root2.left)and
            areIdentical(root1.right, root2.right) 
            )    

#Wrong Outputs To be Reviewed
'''def ino2(T1, T2, f):
    if (T1==None) and (T2!=None):
        f = 0
        return
    if (T1!=None) and (T2==None):
        f = 0
        return
    if (T1==None) and (T2==None):
        return
    ino2(T1.left, T2.left, f)
    if (T1.data!=T2.data):
        f = 0
        return
    ino2(T1.right, T2.right, f)


def ino1(T1, T2, f):
    if (T1==None):
        return
    if (T1.data==T2.data):
        ff=1
        ino2(T1, T2, ff)
        if (ff==1):
            f = 1
    ino1(T1.left, T2, f)
    ino1(T1.right, T2, f)

def isSubTree(T1, T2):
    f = 0
    ino1(T1, T2, f)
    if (f==1):
        return True
    else:
        return False'''
    
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        rootT=buildTree(input())
        rootS=buildTree(input())
        if isSubTree(rootT, rootS) is True:
            print("1")
        else:
            print("0")
# } Driver Code Ends
