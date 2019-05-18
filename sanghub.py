class ShNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class SList:
    
    def __init__(self):
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)
        self.size = 0 
    
    def push(self, value):
        if self.size == 0:
            self.head.next = Node(value, None)
            self.tail = self.head.next
        else:
            self.tail.next = Node(value, None)
            self.tail = self.tail.next
        self.size += 1
    
    def search(self, value):
        point = self.head.next
        if point == None:
            print("search error: The size is 0")
            return False
        else:
            while True:
                if point == None:
                    print("Search Error: the position values None")
                    return False
                elif point.value == value:
                    return point
                else:
                    point = point.next
                    
    def insert_front(self, value):
        self.head.next = Node(value, self.head.next)
        self.size += 1
        
    def insert_after(self, pre_val, value):
        point = self.search(pre_val)
        if point:
            point.next = Node(value, point.next)
            self.size += 1
        else:
            print("insert error: unable to work")
        
    def delete_front(self):
        if self.size != 0:
            self.head.next = self.head.next.next
            self.size -= 1
        else:
            print("delete error: unable to work")
        
    def delete_after(self, value):
        point = self.search(value)
        if point:
            point.next = point.next.next
            self.size -= 1
        else:
            print("delete error: unable to work")
        
    def printSList(self):
        point = self.head
        print("[head]", end="")
        while True:
            print(" ->", point.next.value, end="")
            point = point.next
            if point.next == None:
                print(" : size=", self.size)
                break


if __name__ == "__main__":
    print('"Making list"')
    testList = SList()
    testList.push(1)
    testList.push(2)
    testList.push(4)
    testList.printSList()
    print()
    print('"Search non existing value,"')
    testList.search(6)
    print()
    print('"insert node 0 in front"')
    testList.insert_front(0)
    testList.printSList()
    print()
    print('"insert node 5 after the node 1"')
    testList.insert_after(1, 5)
    testList.printSList()
    print()
    print('"delete front node"')
    testList.delete_front()
    testList.printSList()
    print()
    print('"delete node 4 after the node 2"')
    testList.delete_after(2)
    testList.printSList()