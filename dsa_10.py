from xml.dom.minidom import Node

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        new_node = Node(data,self.head)
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    
    def insert_at_pos(self, data, val):
        new_node = Node(data)
        temp = self.head
        while temp:
            if temp.data != val:
                temp = temp.next
            else:
                new_node.next = temp.next
                temp.next = new_node
                break
            
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print(None)

L1 = LinkedList()
L1.insert_at_beginning(10)
L1.insert_at_beginning(20)
L1.insert_at_beginning(100)
L1.insert_at_end(14)
L1.insert_at_end(90)
L1.display()