class Node:
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_the_beginning(self, data) -> None:
        self.head = Node(data, self.head)

    def insert_at_the_end(self, data) -> None:
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def remove_from_beginning(self):
        if self.head is None:
            return
        removedData = self.head.data
        self.head = self.head.next
        return removedData

    def remove_at_the_end(self):
        if self.head is None:
            return
        itr = self.head
        while itr.next.next:
            itr = itr.next
        removedData = itr.next.data
        itr.next = None
        return removedData

    def length(self):
        itr = self.head
        length = 0
        while itr:
            length += 1
            itr = itr.next
        return length

    def print_list(self):
        if self.head is None:
            print('List is empty')
            return
        itr = self.head
        res = 'Start--->'
        while itr:
            res += str(itr.data) + '--->'
            itr = itr.next
        print(res)

    def insert_after_value(self, afterValue, data):
        if self.head is None:
            print('List is empty')
            return
        itr = self.head
        while itr:
            if itr.data == afterValue:
                itr.next = Node(data, itr.next)
                return
            itr = itr.next
        print('Given search value doesn\'t exists')

if __name__ == '__main__':
    ll = SingleLinkedList()
    ll.insert_at_the_beginning(30)
    ll.insert_at_the_beginning(40)
    ll.insert_at_the_beginning(50)
    ll.insert_at_the_end(20)
    ll.insert_at_the_end(10)
    # ll.remove_from_beginning()
    ll.print_list()
    ll.insert_after_value(20, 15)
    # print(str(ll.length()))
    # print('After deletion from the end')
    # ll.remove_at_the_end()
    ll.print_list()