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
        sl.printAll()

    def test_push(self):
        sl = SingleLinkedList()
        assert sl.tot_length == 0
        sl.push(Node('apple'))
        sl.push(Node('banana'))
        sl.push(Node('orrange'))
        assert sl.tot_length == 3

    # def test_sh_push(self):
    #     sh = SList()
    #     sh.push('apple')
    #     sh.push('banana')
    #     sh.push('orange')
    #     assert sh.size == 3
    #     sh.printSList()
    
    def test_pop(self):
        sl = SingleLinkedList()
        sl.push(Node('apple'))
        sl.push(Node('banana'))
        sl.push(Node('orrange'))
        assert sl.pop().value == 'orrange'
        assert sl.pop().value == 'banana'
        assert sl.pop().value == 'apple'
        assert sl.tot_length == 0

    def test_node(self):
        Node('apple')
