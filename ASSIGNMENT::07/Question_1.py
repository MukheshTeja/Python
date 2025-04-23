class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None  

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def remove(self, data):
        temp = self.head
        if temp and temp.data == data:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next 
        if temp:
            prev.next = temp.next

    def display(self):

        temp = self.head
        while temp:
            print(temp.data,
            temp = temp.next
        print('None')

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.display()
ll.remove(2)
ll.display()
