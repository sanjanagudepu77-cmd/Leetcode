# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive approach
        '''res = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)     # Left
            res.append(node.val)   # Root
            inorder(node.right)    # Right
        inorder(root)
        return res'''
        res = []
        stack = []
        curr = root
        while curr or stack:
            # go to leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
            # process node
            curr = stack.pop()
            res.append(curr.val)
            # move to right subtree
            curr = curr.right
        return res