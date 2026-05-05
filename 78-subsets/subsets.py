class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''n=len(nums)
        res=[]
        for val in range(1<<n):
            s=[]
            for j in range(n):
                if val&(1<<j):
                    s.append(nums[j])
            res.append(s)
        return res'''
        def generate(ind,subset,ans,nums):
            if(ind==len(nums)):
                ans.append(subset.copy())
                return
            subset.append(nums[ind])
            generate(ind+1,subset,ans,nums)
            subset.pop()
            generate(ind+1,subset,ans,nums)
        ind=0
        ans=[]
        subset=[]
        generate(ind,subset,ans,nums)
        return ans
        