# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        # Search for node
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # Node with one or no child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Node with two children
            pre = self.pred(root.left)
            # Replace with predecessor value
            root.val = pre.val
            # Delete predecessor
            root.left = self.deleteNode(root.left, pre.val)
        return root
    def pred(self, root):
        while root.right:
            root = root.right
        return root