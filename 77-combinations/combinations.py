class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(ind,res,ans):
            if len(res)==k:
                ans.append(res.copy())
                return
            for num in range(ind,n+1):
                res.append(num)
                backtrack(num+1,res,ans)
                res.pop()
        ans=[]
        res=[]
        ind=1
        backtrack(ind,res,ans)
        return ans    
          
        