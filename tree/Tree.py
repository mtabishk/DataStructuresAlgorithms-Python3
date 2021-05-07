class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def add_child(self, node):
        self.children.append(node)

