class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        ptr = 1 
        c = 1    
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                c += 1
            else:
                c = 1
            if c <= 2:
                nums[ptr] = nums[i]
                ptr += 1
        return ptr