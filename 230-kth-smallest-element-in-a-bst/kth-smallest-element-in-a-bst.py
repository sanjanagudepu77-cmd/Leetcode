# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.c=0
        self.res=0
        def inorder(root):
            if root:
                inorder(root.left)
                self.c+=1
                if self.c==k:
                    self.res=root.val
                inorder(root.right)
        inorder(root)
        return self.res
                    
        

        