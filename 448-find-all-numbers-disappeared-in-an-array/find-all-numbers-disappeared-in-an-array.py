class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums=set(nums)
        res=[]
        for num in range(1,n+1):
            if num not in nums:
                res.append(num)
        return res 

        