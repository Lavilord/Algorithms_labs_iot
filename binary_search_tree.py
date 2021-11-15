class Tree:

    def __init__(self):
        self.root = None

    def search(self, value):
        found_node = self._search(self.root, value)
        if found_node is None:
            return False
        return True

    def search_node(self, value):
        found_node = self._search(self.root, value)
        return found_node

    def delete(self, value):
        node_to_delete = self.search_node(value)
        if node_to_delete is None:
            print("there are no nodes with such values")
        else:
            self._delete(node_to_delete)

    def _delete(self, current_node):
        # if we are deleting root:
        if (current_node == self.root):
            if (current_node.right is None):
                if (current_node.left is None):
                    self.root = None
                else:
                    self.root = current_node.left
            else:
                if (current_node.left is None):
                    self.root = current_node.right
                if (current_node.left is not None):
                    self.delete_node_with_two_childs(current_node)
        # if we are deleting anything but root
        else:
            if (current_node.value > current_node.parent.value):
                if (current_node.left is not None and current_node.right is not None):
                    self.delete_node_with_two_childs(current_node)
                else:
                    current_node.parent.right = self.attach_leaf(current_node)
            else:
                if (current_node.left is not None and current_node.right is not None):
                    self.delete_node_with_two_childs(current_node)
                else:
                    current_node.parent.left = self.attach_leaf(current_node)

    def delete_node_with_two_childs(self, current_node):
        change_node = self.node_to_change(current_node.right)
        change_node_value = change_node.value
        self.delete(change_node_value)
        current_node.value = change_node_value


    def attach_leaf(self, current_node):
        if (current_node.left is None and current_node.right is None):
            return None

        if (current_node.left is not None and current_node.right is None):
            current_node.left.parent = current_node.parent
            return current_node.left

        if (current_node.left is None and current_node.right is not None):
            current_node.right.parent = current_node.parent
            return current_node.right


    def node_to_change(self, current_node):
        if current_node.left:
            return self.node_to_change(current_node.left)
        else:
            return current_node


    def min_in_right_(self):
        root_node = search_node(self.root)
        _min_in_right_tree(root_node.right)


    def _min_in_right_tree(self, min_node):
        if min_node.left is not None:
            _min_in_right_tree(min_node.left)
        else:
            return min_node


    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        return self._insert(self.root, value)


    def _insert(self, current_node, value):
        if (value > current_node.value):
            # add to the right
            if current_node.right is None:
                current_node.right = Node(value, current_node)
                return
            return self._insert(current_node.right, value)

        else:
            # add to the left
            if current_node.left is None:
                current_node.left = Node(value, current_node)
                return
            return self._insert(current_node.left, value)


    def _search(self, node_to_check, value):
        if (node_to_check is None) or (node_to_check.value == value):
            return node_to_check

        if value > node_to_check.value:
            # go right
            return self._search(node_to_check.right, value)
        else:
            # go left
            return self._search(node_to_check.left, value)


    def insert_with_search(self, current_node, value):
        found_node = self._search(current_node, value)


    def print_the_tree(self):
        self._print_the_tree(self.root)


    def _print_the_tree(self, current_node):
        print(current_node.value)
        if current_node.right is not None:
            self._print_the_tree(current_node.right)
        if current_node.left is not None:
            self._print_the_tree(current_node.left)


class Node:

    def __init__(self, value, parent=None):
        self.right = None
        self.left = None
        self.parent = parent
        self.value = value

if __name__ == '__main__':
    tree = Tree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(8)
    tree.insert(6)
    tree.insert(10)
    tree.insert(12)
    tree.insert(7)
    tree.insert(4)
    tree.insert(3)
    tree.insert(4)
    tree.insert(1)
    tree.print_the_tree()

    print(tree.search(6))
    print(tree.search(7))
    print(tree.search(2))
    print(tree.search(5))
    tree.delete(5)
    tree.delete(6)
    tree.delete(8)
    tree.delete(2)

    print(tree.search(7))
    print(tree.root.value)
    tree.print_the_tree()
