class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res=[]
        n=len(nums)
        for i in range(n):
            if nums[i]!=val:
                res.append(nums[i])
        for i in range(len(res)):
            nums[i] = res[i]
        
        return len(res)
         
        