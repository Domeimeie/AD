class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:

    def __init__(self):
        self.root_node = None

    def insert(self, data):
        if self.root_node is None:    
            self.root_node = Node(data)
            return
        
        current = self.root_node
        while True:
            if current.data > data:
                if current.left_child is None:
                    current.left_child = Node(data)
                    return
                else:
                    current = current.left_child
            elif current.data < data:
                if current.right_child is None:
                    current.right_child = Node(data)
                    return
                else:
                    current = current.right_child
            else:
                return

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current.data

    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child
        return current.data

    def print(self):
        self._print_node(self.root_node)

    def _print_node(self, node, level=0):
        if node is not None:
            self._print_node(node.right_child, level + 1)
            print(' ' * 4 * level + f'-> {node.data}')
            self._print_node(node.left_child, level + 1)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(30)
    bst.insert(2)
    bst.insert(40)
    bst.insert(25)
    bst.insert(4)
    assert bst.root_node.data == 5
    assert bst.find_min() == 2
    assert bst.find_max() == 40
    bst.print()
    print("-" * 20)
