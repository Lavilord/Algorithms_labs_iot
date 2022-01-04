
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL():

    def insert(self, root, value):

        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance = self.getBalance(root)

        #Left Left
        if balance > 1 and value < root.left.value:
            return self.rightRotate(root)

        # Right Right
        if balance < -1 and value > root.right.value:
            return self.leftRotate(root)

        #Left Right
        if balance > 1 and value > root.left.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        #Right Left
        if balance < -1 and value < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def delete(self, root, value):


        if not root:
            return root

        elif value < root.value:
            root.left = self.delete(root.left, value)

        elif value > root.value:
            root.right = self.delete(root.right, value)

        else:
            if root.left is None:
                temp_node = root.right
                root = None
                return temp_node

            elif root.right is None:
                temp_node = root.left
                root = None
                return temp_node

            temp_node = self.getMinNode(root.right)
            root.value = temp_node.val
            root.right = self.delete(root.right,
                                     temp_node.value)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance = self.getBalance(root)

        #Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        #Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        #Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        #Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinNode(root.left)

    def print_tree(self, root):

        if not root:
            return

        print(root.value)
        self.print_tree(root.left)
        self.print_tree(root.right)


tree = AVL()
root = None
nodes = [12, 9, 5, 10, 0, 6, 11, -1, 1, 2]
for node in nodes:
    root = tree.insert(root, node)

tree.print_tree(root)

root = tree.delete(root, 12)
print('###########################################################')
tree.print_tree(root)
