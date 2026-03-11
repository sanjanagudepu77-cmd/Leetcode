class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)    
        right = sum(nums)   
        while left <= right:
            mid=(left+right)//2   
            curr=0    
            splits = 1
            for n in nums:
                if curr+n>mid:
                    splits+= 1
                    curr=0
                curr += n 
            if splits > k:
                left = mid+1
            else:
                right = mid-1
        return left 
        