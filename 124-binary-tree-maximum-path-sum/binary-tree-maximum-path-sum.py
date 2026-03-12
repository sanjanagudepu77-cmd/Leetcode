# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxcurr=float('-inf')
        def help(node):
            if not node:
                return 0
            lt=max(help(node.left),0)
            rt=max(help(node.right),0)
            curr=node.val+lt+rt
            self.maxcurr=max(self.maxcurr,curr)
            return max(lt,rt)+node.val
        help(root)
        return self.maxcurr
        