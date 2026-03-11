class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if(nums[i]+nums[j]==target):
                   return [i,j]
        '''n=len(nums)
        left = 0
        right =n-1
        while left < right:
            if nums[left]+ nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1'''