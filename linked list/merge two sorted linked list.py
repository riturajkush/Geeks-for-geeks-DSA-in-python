#User function Template for python3
'''
	Function to merge two sorted lists in one
	using constant space.
	
	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
def merge(head_a,head_b):
    head_ptr = temp_ptr = Node()
    while head_a or head_b:
        if head_a and (not head_b or head_a.data<=head_b.data):
            temp_ptr.next = Node(head_a.data)
            head_a = head_a.next
        else:
            temp_ptr.next = Node(head_b.data)
            head_b = head_b.data
        temp_ptr = temp_ptr.next
    return head_ptr.next
'''

#{ 
#  Driver Code Starts
#Initial Template for Python 3
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
        n,m = map(int, input().strip().split())
        a = LinkedList() # create a new linked list 'a'.
        b = LinkedList() # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)
        for x in nodes_b:
            b.append(x)
        a.head = merge(a.head,b.head)
        a.printList()
# } Driver Code Ends
