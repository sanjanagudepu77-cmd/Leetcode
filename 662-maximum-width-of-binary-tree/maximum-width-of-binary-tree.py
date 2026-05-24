# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=[(root,0)]
        max_width=0
        while q:
            n=len(q)
            first = q[0][1]     # first index of level
            for i in range(n):
                node,index=q.pop(0)
                # normalize index to avoid very large numbers
                index-=first
                if i==0:
                    left = index
                if i==n-1:
                    right=index
                if node.left:
                    q.append((node.left,2*index)) #1 based indexing formula for l and r
                if node.right:
                    q.append((node.right,2*index+1))
            max_width=max(max_width,right-left+1)
        return max_width

        