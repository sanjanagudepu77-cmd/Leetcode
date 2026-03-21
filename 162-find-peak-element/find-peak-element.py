class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''n=len(nums)
        for i in range(n - 1):
            curr = nums[i]
            if curr > nums[i + 1]:
                return i
        return n - 1'''
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                r=mid
        return l

        