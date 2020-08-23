#User function Template for python3
'''
Function Arguments :
		@param  : head (given head of linked list), k(value of k)
		@return : None, Just swap the nodes
		
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
def swapkthnode(head,num,k):
    
    if (num<k):
        return
    if ((num%2!=0) and ((num//2+1)==k)):
        return
    curr1 = head
    curr1_prev = Node(None)
    for i in range(k-1):
        curr1_prev = curr1
        curr1 = curr1.next
    curr2 = head
    curr2_prev = Node(None)
    for i in range(num-k):
        curr2_prev = curr2
        curr2 = curr2.next
    #print("@@@@",curr1_prev.data, curr2_prev.data)    
    if curr1_prev:
        curr1_prev.next = curr2
    if curr2_prev:
        curr2_prev.next = curr1
        
    temp = curr1.next
    curr1.next = curr2.next
    curr2.next = temp
    

    
    if (k==1):
        #print(head)
        head = curr2
         
    if (k==num):
        #print(head)
        head = curr1
        
    curr = head
    for i in range(num):
        #print(curr.data,end="")
        curr = curr.next


#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

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
        
# returns the nth node from end.
def getNthfromEnd(head, n):
    # using two pointers, similar to finding middle element
    curr_node = head
    nth_node = head

    while n:
        if n and curr_node == None:
            return None
        curr_node = curr_node.next
        n -= 1

    while curr_node:
        curr_node = curr_node.next
        nth_node = nth_node.next

    return nth_node


# returns the nth node from beg.
def getNthfromBeg(head, n):
    curr_node = head
    for i in range(n - 1):
        if curr_node is None:
            return None
        else:
            curr_node = curr_node.next

    return curr_node

if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, kth_node = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        # intial nodes at respective positions.
        check = [getNthfromBeg(a.head, kth_node), getNthfromEnd(a.head, kth_node)]

        swapkthnode(a.head,n, kth_node)

        new_check = [getNthfromEnd(a.head, kth_node), getNthfromBeg(a.head, kth_node)]
        if (check == new_check):
            print(1)
        else:
            print(0)
# } Driver Code Ends
