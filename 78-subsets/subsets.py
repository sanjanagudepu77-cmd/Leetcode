class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        for val in range(1<<n):
            s=[]
            for j in range(n):
                if val&(1<<j):
                    s.append(nums[j])
            res.append(s)
        return res
        