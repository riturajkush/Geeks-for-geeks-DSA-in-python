#User function Template for python3
'''
	Function to add two numbers represented 
	in the form of the linked list.
	
	Function Arguments: head_a and head_b (heads of both the linked lists)
	Return Type: head of the resultant linked list.
    
    __>IMP : numbers are represented in reverse in the linked list.
    Ex:
        145 is represented as  5->4->1.
    
    resultant head is expected in the same format.
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
def addBoth(l1, l2):
    sum = l1.data + l2.data
    carry = int(sum / 10)
 
    l3 = Node(sum%10)
    p1 = l1.next
    p2 = l2.next
    p3 = l3
    while(p1 != None or p2 != None):
        sum = carry + ( p1.data if p1 else 0) + ( p2.data if p2 else 0)
        carry = int(sum//10)
        p3.next = Node(sum % 10)
        p3 = p3.next
        p1 = p1.next if p1 else None
        p2 = p2.next if p2 else None
 
    if(carry > 0):
        p3.next = Node(carry)
 
    return l3
        


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
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n_a = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_a = nodes_a[::-1] # reverse the input array
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        n_b =int(input())
        b = LinkedList()  # create a new linked list 'b'.
        nodes_b = list(map(int, input().strip().split()))
        nodes_b = nodes_b[::-1]  # reverse the input array
        for x in nodes_b:
            b.append(x)  # add to the end of the list

        result_head = addBoth(a.head,b.head)
        printList(result_head)
# } Driver Code Ends
