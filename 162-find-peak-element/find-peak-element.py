class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''n=len(nums)
        for i in range(n - 1):
            curr = nums[i]
            if curr > nums[i + 1]:
                return i
        return n - 1'''
        
        n = len(nums)

        if n == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[n - 1] > nums[n - 2]:
            return n - 1

        l = 1
        h = n - 2

        while l <= h:
            mid = (l + h) // 2

            # peak found
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            # increasing slope → move right
            elif nums[mid] > nums[mid - 1]:
                l = mid + 1

            # decreasing slope → move left
            else:
                h = mid - 1

        return -1

        