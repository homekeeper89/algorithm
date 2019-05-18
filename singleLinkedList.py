# Node 
class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None

class SingleLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.tot_length = 0
<<<<<<< HEAD
=======
    
    def lastNode(self):
        temp_node = self.head
        last_node = ''
        before_last_node = ''
        for i in range(self.tot_length +1):
            if i == self.tot_length - 1:
                before_last_node = temp_node
                last_node = temp_node.next
            temp_node = temp_node.next
        return before_last_node, last_node
>>>>>>> 2393c7c47030e886bd51006c26167cce34cd750c

    def push(self, node):
        if self.tot_length == 0:
            self.head.next = node
            node.next = self.tail
        else:
            temp_node = self.head
            for i in range(self.tot_length +1):
                if temp_node.next.value is None:
                    temp_node.next = node
                    node.next = self.tail
                temp_node = temp_node.next
        self.tot_length += 1
    
    def pop(self):
        if self.tot_length == 0:
            return None
        else:
            before_last_node, last_node = self.lastNode()
            before_last_node.next = self.tail
            self.tot_length -= 1
        return last_node

    def insert(self, position, node):
        pass

    def printAll(self):
        temp_node = self.head
        for i in range(self.tot_length):
            if temp_node.next is None:
                print('end')
                break
            print(i, temp_node.next.value)
            temp_node = temp_node.next

        