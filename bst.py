class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, value):
        if self is None or value == self.data:
            return
        if value > self.data:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)

    def get_level(self):
        l = -1
        itr = self
        while itr:
            l += 1
            if itr.left is not None:
                itr = itr.left
            elif itr.right is not None:
                itr = itr.right
            else:
                itr = None
        return l

    def in_order_traversal(self):
        if self is None:
            return
        elements = []
        if self.left is not None:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right is not None:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        if self is None:
            return
        elements = []
        elements.append(self.data)
        if self.left is not None:
            elements += self.left.in_order_traversal()
        if self.right is not None:
            elements += self.right.in_order_traversal()
        return elements
    
    def post_order_traversal(self):
        if self is None:
            return
        elements = []
        if self.left is not None:
            elements += self.left.post_order_traversal()
        if self.right is not None:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def search_value(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.search_value(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search_value(value)

    def find_min(self):
        if self is None:
            return
        if self.left is not None:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self is None:
            return
        if self.right is not None:
            return self.right.find_max()
        return self.data

    def calculate_sum(self):
        if self is None:
            return 0
        sum = 0
        elements = self.in_order_traversal()
        for el in elements:
            sum += el
        return sum

    # def delete_node(self, value):
    #     if value > self.data:
    #         self.right = self.right.delete_node(value)
    #     elif value < self.data:
    #         self.left = self.left.delete_node(value)
    #     else:
    #         if self.left is None and self.right is None:
    #             return
    #         if self.left is not None:
    #             max_val = self.left.find_max()
    #             self.left = self.left.delete_node(max_val)

    def delete_node(self, value):
        if value > self.data:
            if self.right:
                self.right = self.right.delete_node(value)
        elif value < self.data:
            if self.left:
                self.left = self.left.delete_node(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_node(min_val)
        return self
            

def build_bst(data):
    root = Node(data[0])
    for i in range(1, len(data)):
        root.insert(data[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 10, 34, 22, 2, 12, 9, 3, 45]
    tree = build_bst(numbers)
    print(tree.in_order_traversal())
    print(tree.pre_order_traversal())
    print(tree.post_order_traversal())
    print(tree.search_value(4))
    print(tree.search_value(41))
    print(tree.find_min())
    print(tree.find_max())
    print(tree.calculate_sum())
    tree.delete_node(10)
    print(tree.in_order_traversal())