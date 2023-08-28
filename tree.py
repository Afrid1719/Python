class TreeNode:
    def __init__(self, data = None) -> None:
        self.data = data
        self.children = []
        self.parent = None
        self.height = 0

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_data(self, type):
        return self.data

    def print_tree(self, type = None):
        level = self.get_level()
        indent = ['  ' for _ in range(level)]
        liner = ''
        if self.parent is not None:
            liner = '|__'
        indent = ''.join(indent) + liner
        print(indent + self.print_data(type))
        if len(self.children) == 0:
            return
        for node in self.children:
            node.print_tree(type)

class ManagementTreeNode(TreeNode):
    def __init__(self, data = None):
        super().__init__(data)

    def print_tree(self, type):
        return super().print_tree(type)

    def print_data(self, type):
        if type == 'name':
            return self.data['name']
        elif type == 'designation':
            return self.data['designation']
        else:
            return f"{self.data['name']} ({self.data['designation']})"

def build_management_tree():
    root = ManagementTreeNode({
        'name': 'Person 1',
        'designation': 'CEO'
    })

    # Level 1
    cto = ManagementTreeNode({
        'name': 'Person 2',
        'designation': 'CTO'
    })
    cfo = ManagementTreeNode({
        'name': 'Person 3',
        'designation': 'CFO'
    })
    cpo = ManagementTreeNode({
        'name': 'Person 3',
        'designation': 'CPO'
    })

    root.add_child(cto)
    root.add_child(cfo)
    root.add_child(cpo)

    #Level 2
    director = ManagementTreeNode({
        'name': 'Person 4',
        'designation': 'Director'
    })
    po1 = ManagementTreeNode({
        'name': 'Person 5',
        'designation': 'PO'
    })
    po2 = ManagementTreeNode({
        'name': 'Person 6',
        'designation': 'PO'
    })
    fm = ManagementTreeNode({
        'name': 'Person 7',
        'designation': 'Finance Manager'
    })

    cto.add_child(director)
    cpo.add_child(po1)
    cpo.add_child(po2)
    cfo.add_child(fm)

    #Level 3

    return root

def build_tree():
    root = TreeNode('Electronics')

    # Level 1
    laptop = TreeNode('Laptop')
    mobile = TreeNode('Mobile')
    camera = TreeNode('Camera')

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(camera)

    # Level 2
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Dell'))
    laptop.add_child(TreeNode('HP'))

    mobile.add_child(TreeNode('IPhone')) 
    mobile.add_child(TreeNode('One Plus')) 
    mobile.add_child(TreeNode('Samsung')) 
    mobile.add_child(TreeNode('Oppo'))

    camera.add_child(TreeNode('Sony'))
    camera.add_child(TreeNode('LG'))

    return root
    
if __name__ == '__main__':
    root = build_management_tree()
    root.print_tree('name')
    root.print_tree('designation')
    root.print_tree('both')
