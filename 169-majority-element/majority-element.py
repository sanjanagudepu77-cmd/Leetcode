'''class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[(len(nums))//2]'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        res=nums[0]
        for i in range(len(nums)):
            if count==0:
                res=nums[i]
            if nums[i]==res:
                count+=1
            else:
                count-=1
        return res
        