class TreeNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
    
    def add_left_subtree(self, node):
        self.left = node

    def add_right_subtree(self, node):
        self.right = node

    def print_tree(self, level = 0):
        if self.data is None:
            return
        print(self.data)
        if self.left is not None:
            print(self.left.data)
        if self.right is not None:
            print(self.right.data)
        self.left.print_tree(level + 1)
        self.right.print_tree(level + 1)

def build_tree():
    root = TreeNode('Data')

    root.add_left_subtree(TreeNode('Binary'))
    root.add_right_subtree(TreeNode('Non-Binary'))

    return root

if __name__ == '__main__':
    tree = build_tree()
    tree.print_tree()