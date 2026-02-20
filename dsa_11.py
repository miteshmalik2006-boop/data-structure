
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def del_at_end(self):
    temp = self.head
    if not self.head:
        return
    if self.head.next is None:
        self.head = None
        return
    
    while temp.next.next:
        temp = temp.next
    temp.next = None

def del_at_beginning(self):
    if not self.head:
        return
    if not self.head.next:
        self.head=None
        return
    self.head = self.head.next


class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def del_third_node(head):
    if head is None or head.next is None or head.next.next is None:
        return head
    
    head.next.next = head.next.next.next
    return head

def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    
head = node(201)
head.next = node(202)
head.next.next = node(203)
head.next.next.next = node(204)
print_list(head)

head = del_third_node(head)
print_list(head)
