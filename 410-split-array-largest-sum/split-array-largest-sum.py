class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return -1
        def canSplit(maxSum):
            count = 1
            curr_sum = 0
            for num in nums:
                if curr_sum + num <= maxSum:
                    curr_sum += num
                else:
                    count += 1
                    curr_sum = num
                if count>k:
                    return False
            return True
        low = max(nums)
        high = sum(nums)
        ans=high
        while low<=high:   
            mid = (low + high) // 2
            if canSplit(mid):
                ans=mid
                high = mid-1
            else:
                low = mid + 1
        return ans
        
        
        '''left = max(nums)    
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
        return left'''
        