# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        def dfs(node, par):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        q = [(target, 0)]
        visited = {target}
        ans = []
        while q:
            node, dist = q.pop(0)
            if dist == k:
                ans.append(node.val)
            if dist < k:
                for i in [node.left, node.right, parent[node]]:
                    if i and i not in visited:
                        visited.add(i)
                        q.append((i, dist + 1))
        return ans


        