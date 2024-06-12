class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if key < root.val:
                root.left = self._insert(root.left, key)
            else:
                root.right = self._insert(root.right, key)
        return root

    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.val)
            res = res + self.inorder_traversal(root.right)
        return res

# Example Usage
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print(bst.inorder_traversal(bst.root))  # Output: [20, 30, 40, 50, 60, 70, 80]