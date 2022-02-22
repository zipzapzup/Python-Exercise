# Implement Singly Linked List
# Using a stack based LIFO mechanisms
# You need to initialise the LinkedList from the end to the start. I.E. Sunday -> Monday

# O(1) Time and Space
class Node(object):
    def __init__(self, data):
        self.value = data
        self.next = None
        # pointer to value, and next

class LinkedList(object):
    def __init__(self, node):
        # Pointer to keep track of the head of the node
        self.head = node
        self.counter = 0

    # O(1) Time Complexity, O(N) Space complexity
    def insert(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    # O(N) Time Complexity, O(1) Space Complexity
    def printList(self):
        print("Starting Print List")
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next

    # Simple fun stuff with iterable
    def __iter__(self):
        return self
    
    def __next__(self):
        currentNode = self.head
        if currentNode:
            print(currentNode.value)
            self.head = currentNode.next
            return self
        else:
            raise StopIteration

Weekdays = LinkedList(Node('Monday'))
Weekdays.insert('Tuesday')
Weekdays.insert('Wednesday')
Weekdays.insert('Thursday')
Weekdays.insert('Friday')
Weekdays.insert('Saturday')
Weekdays.insert('Sunday')

Weekdays.printList()
Weekdays.printList()
print("Looping .......")
for i in Weekdays:
    pass