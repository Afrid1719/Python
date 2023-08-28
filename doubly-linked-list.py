class Node:
    def __init__(self, data = None, prev = None, next = None) -> None:
        self.data = data
        self.prev = prev
        self.next = next
    
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_beginning(self, data = None) -> None:
        prevNode = self.head
        self.head = Node(data, None, self.head)
        if prevNode is not None:
            prevNode.prev = self.head
        
    def insert_at_end(self, data = None) -> None:
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, itr, None)
    
    def print_forward(self) -> None:
        res = 'Going Forward-->'
        itr = self.head
        while itr:
            res += str(itr.data) + '-->'
            itr = itr.next
        print(res)

    def print_backward(self) -> None:
        res = 'Going Backward-->'
        itr = self.head
        while itr.next:
            itr = itr.next
        while itr:
            res += str(itr.data) + '-->'
            itr = itr.prev
        print(res)

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_beginning(45)
    dll.insert_at_beginning(35)
    dll.insert_at_beginning(25)
    dll.insert_at_end(55)
    dll.insert_at_end(65)
    dll.print_forward()
    dll.print_backward()