#Node class will represent the node in linked list.
#Each node will contain key-value pair and the pointer to the next node
class Node:  
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None 
        

#HashTable class will contain the array that will hold the linked lists as well as the methods to insert, retrieve and delete 
#datas from the hash tables
class HashTable:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity


#_hash method takes key and returns an index in the array where key-value pair should be stored.
def _hash(self, key):
    return hash(key) % self.capacity


def insert(self, key, value):
    index = self._hash(key)
    
    if self.table[index] is None:
        self.table[index] = Node(key, value)
        self.size += 1
    else:
        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.size += 1
        
    
