from . import *

class TestSingle:

    def test_node(self):
        node = Node()
        assert node.next == None
    
    def test_single(self):

        sl = SingleLinkedList()
        assert sl.tot_length == 0
        sl.push(Node('apple'))
        sl.push(Node('banana'))
        assert sl.tot_length == 2
        # sl.printAll()
        sl.test()
