# Class to represent a node
'''class StackNode:

	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None'''
		
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        if (self.head==None):
            self.head = StackNode(data)
        else:
            new_node = StackNode(data)
            new_node.next = self.head
            self.head = new_node
            
    def pop(self):
        '''if (self.head.data==None or self.head==None):
            return -1'''
        try:
            val = self.head.data
            self.head = self.head.next
            return val
        except:
            return -1




#{ 
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = Stack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()

# } Driver Code Ends# Class to represent a node
'''class StackNode:

	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None'''
		
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        if (self.head==None):
            self.head = StackNode(data)
        else:
            new_node = StackNode(data)
            new_node.next = self.head
            self.head = new_node
            
    def pop(self):
        '''if (self.head.data==None or self.head==None):
            return -1'''
        try:
            val = self.head.data
            self.head = self.head.next
            return val
        except:
            return -1




#{ 
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = Stack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()

# } Driver Code Ends
