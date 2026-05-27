# Understanding Graphs and Trees
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return
        self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = TreeNode(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = TreeNode(value)

    def inorder(self, node=None):
        if node is None:
            node = self.root
        result = []
        if node.left:
            result.extend(self.inorder(node.left))
        result.append(node.value)
        if node.right:
            result.extend(self.inorder(node.right))
        return result

bst = BinarySearchTree()
for v in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(v)
print(f"Inorder: {bst.inorder()}")
