class Node:
    def __init__(self, head = None,next = None,prev = None):
        self.head = head
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self,head = None):
        self.head = head

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node


    def display(self):
        temp = self.head
        while temp:
            print(temp.head,end = "<->")
            temp = temp.next

l1 = DoublyLinkedList()
l1.insert_at_Begining(15)
l1.insert_at_Begining(17)
l1.display()
