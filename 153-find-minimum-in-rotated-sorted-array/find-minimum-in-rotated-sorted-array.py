class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''return min(nums)'''
        '''low, high = 0, len(nums) - 1
        while low <= high:
            if nums[low] <= nums[high]:
                return nums[low]
            mid = (low + high)//2
            if nums[low] > nums[mid]:
                high = mid
            else:
                low = mid + 1
        low,high=0,len(nums)-1
        while low<=high:
            if nums[low]<=nums[high]:
                return nums[low]'''
        n = len(nums)
        l = 0
        h = n - 1
        ans = float('inf')
        
        while l <= h:
            mid = (l + h) // 2
            
            # If left part is sorted
            if nums[l] <= nums[mid]:
                ans = min(ans, nums[l])   # leftmost is minimum in this part
                l = mid + 1
            else:
                ans = min(ans, nums[mid]) # mid could be minimum
                h = mid - 1
        
        return ans