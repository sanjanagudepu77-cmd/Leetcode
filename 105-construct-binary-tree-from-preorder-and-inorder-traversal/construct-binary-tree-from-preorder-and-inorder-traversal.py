# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''inorder_map={}
        for i in range(len(inorder)):
            inorder_map[inorder[i]]=i
        self.pre_index=0
        def helper(left,right):
            if left>right:
                return None
            root_val=preorder[self.pre_index]
            self.pre_index+=1
            root=TreeNode(root_val)
            mid=inorder_map[root_val]
            root.left=helper(left,mid-1)
            root.right=helper(mid+1,right)
            return root
        return helper(0,len(inorder)-1)'''
        # Store inorder values with index
        inMap = {}
        for i in range(len(inorder)):
            inMap[inorder[i]] = i

        return self.build(
            preorder, 0, len(preorder)-1,
            inorder, 0, len(inorder)-1,
            inMap
        )

    def build(self, preorder, preStart, preEnd,
              inorder, inStart, inEnd, inMap):

        # Base case
        if preStart > preEnd or inStart > inEnd:
            return None

        # Root is first element in preorder
        root = TreeNode(preorder[preStart])

        # Find root in inorder
        inRoot = inMap[root.val]

        # Number of nodes in left subtree
        numsLeft = inRoot - inStart

        # Build left subtree
        root.left = self.build(
            preorder,
            preStart + 1,
            preStart + numsLeft,
            inorder,
            inStart,
            inRoot - 1,
            inMap
        )

        # Build right subtree
        root.right = self.build(
            preorder,
            preStart + numsLeft + 1,
            preEnd,
            inorder,
            inRoot + 1,
            inEnd,
            inMap
        )

        return root
        