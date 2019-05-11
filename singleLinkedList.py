# Node 
class Node:
    def __init__(self, val=None):
        self.next = None
        self.value = val

class SingleLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.tot_length = 0
    
    def push(self, node):
        if self.tot_length == 0:
            self.head.next = node
            node.next = self.tail
        else:
            for i in range(self.tot_length):
                temp_node = self.head
                if temp_node.next.value is None:
                    temp_node.next = node
                    node.next = self.tail
                temp_node = temp_node.next
        self.tot_length += 1

    def insert(self, position, node):
        pass

    def printAll(self):
        for i in range(self.tot_length):
            temp_node = self.head
            if temp_node.next is None:
                print('over')
                break
            print(i, temp_node.next.value)
            temp_node = temp_node.next

        