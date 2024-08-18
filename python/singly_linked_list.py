class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

def insert_at_begining(head, data):
    new_node = Node(data)
    new_node.next = head
    
    return new_node


def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    
    current = head
    while current.next:
        current = current.next
        
    current.next = new_node
    return head

#insert the given data after the specific node
def insert_after_node(node, data):
    if node is None:
        print("Error: The given node is None") 
        return
    
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node

def traverse(head):
    current = head
    while current:
        print(str(current.data) + "->", end = " ")
        current = current.next
    
    print("None")
    

#driver code
head = None
head = insert_at_begining(head, 4)
head = insert_at_begining(head, 3)
head = insert_at_begining(head, 2)
head = insert_at_begining(head, 1)

insert_after_node(head, 5)

head = insert_at_begining(head, 6)

head = insert_at_end(head, 7)

traverse(head)
