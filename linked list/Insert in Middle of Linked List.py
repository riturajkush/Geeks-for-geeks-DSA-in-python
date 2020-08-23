#User function Template for python3
'''
    Your task is to insert a new node in 
	the middle of the linked list with
	the given value.
	
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
	
	Function Arguments: head (head of linked list), node (node to be inserted in middle)
	Return Type: None, just insert the new node at mid.
'''
def insertInMid(head,node):
    temp=head
    p=0
    while temp!=None:
        p+=1
        temp=temp.next
    q=p//2
    if p%2!=0:
        q+=1
    r=1
    temp=head
    while r!=q:
        temp=temp.next
        r+=1
    node.next=temp.next
    temp.next=node
    
    '''curr = head
    count = 1
    while (curr.next!=None):
        curr = curr.next
        count = count + 1
        mid = (count)//2
        if (count%2==0):
            mid = mid-1
        curr = head
        count = 0
        while (count<mid):
            curr = curr.next
            count = count + 1
        node.next = curr.next
        curr.next = node'''
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
    
    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print(' ')

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        mid_elem = int(input())
        insertInMid(a.head, Node(mid_elem) )
        a.printList()
# } Driver Code Ends
