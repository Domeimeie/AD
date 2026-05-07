class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree:

    def __init__(self):
        self.root_node = None

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            while current:
                if data < current.data:
                    if current.left_child is None:
                        break
                    else:
                        current = current.left_child
                else:
                    if current.right_child is None:
                        break
                    else:
                        current = current.right_child
            # now we found parent
            if data < current.data:
                current.left_child = node
            else:
                current.right_child = node

    def remove(self, data):
        parent = None
        current = self.root_node
        while current:
            if current.data == data:
                if parent is None:
                    self.root_node = self.remove_node(current)
                elif current == parent.left_child:
                    parent.left_child = self.remove_node(current)
                else:
                    parent.right_child = self.remove_node(current)
                return
            elif data < current.data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child


    def remove_node(self, node):
        if node is None:
            return None
        if node.left_child is None and node.right_child is None:
            # node has no children
            return None
        if node.left_child is None:
            # node has no left child
            return node.right_child
        if node.right_child is None:
            # node has no right child
            return node.left_child
        # node has both left and right child
        predecessor = self.find_predecessor(node)
        self.remove(predecessor.data)
        node.data = predecessor.data
        return node

    def find_predecessor(self, node):
        current = node.left_child
        while current.right_child:
            current = current.right_child
        return current

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
        # traverse in-order and print nodes
        self._traverse_inorder(self.root_node, True)
        print('\n')
        self._print_node(self.root_node)

    def _traverse_inorder(self, node, do_print=False):
        if node is None:
            return
        else:
            self._traverse_inorder(node.left_child, do_print)
            if do_print:
                print(node.data)
            self._traverse_inorder(node.right_child, do_print)

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
    bst.remove(30)
    bst.print()
    print("-" * 20)
    bst.remove(2)
    bst.print()
    print("-" * 20)
    bst.remove(4)
    bst.print()

