class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq=set()
        n=len(nums)
        for i in range(n):
            if nums[i] in freq:
                return nums[i]
            freq.add(nums[i])
        