# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[(root,0,0)]
        colt=defaultdict(list)
        res=[]
        while q:
            node,row,col=q.pop(0)
            colt[col].append((row,node.val))
            if node.left:
                q.append((node.left,row+1,col-1))
            if node.right:
                q.append((node.right,row+1,col+1))
        for col in sorted(colt.keys()):
            node=sorted(colt[col])# node=sorted(colt[col],key=lambda x:[0],x[1])
            res.append([val for i,val in node]) #for row,val in node
        return res




        