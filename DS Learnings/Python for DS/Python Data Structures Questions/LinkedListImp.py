class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# a = Node(1)
# b = Node(2)
# c = Node(3)
# print(a.data)
# print(a.next)

# a.next = b
# b.next = c
class LinkedList:
    def __init__(self):
        # Empty LinkedList
        self.head = None
        self.n = 0  # no of nodes in likedlist

    def __len__(self):
        return self.n
    
    def insert_at_first(self, value):
        # new node
        new_node = Node(value)

        # create connection
        new_node.next = self.head
        self.head = new_node

        # increament n
        self.n = self.n + 1

    def __str__(self):
        # head is first node
        curr = self.head
        result = ''
        while curr != None:

            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]
    
    def append(self, value):

        new_node = Node(value)
        if self.head == None:
            # empty
            self.head = new_node
            return
        
        curr = self.head
        while curr.next != None:
            curr = curr.next

        # now we at last node
        curr.next = new_node

        # increament n
        self.n = self.n + 1

    # insert after any item in list
    def insert_after(self, after, value):

        # creating new node
        new_node = Node(value)

        curr = self.head

        while curr != None:
            if curr.data == after:
                break

            curr = curr.next
            
        # case 1 - item found and come through break
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
        else:
            return "Item not found"

L = LinkedList()
L.insert_at_first(1)
L.insert_at_first(2)
L.insert_at_first(3)
L.insert_at_first(4)
print(L)
L.insert_after(5, 15)

print(len(L))






