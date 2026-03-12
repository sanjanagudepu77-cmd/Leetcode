class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''count=0
        n=len(nums)
        for i in range(n):
            curr_sum=0
            for j in range(i,n):
                curr_sum+=nums[j]
                if curr_sum==k:
                    count+=1
        return count'''
        ps=0
        freq={0:1}
        ans=0
        for num in nums:
            ps+=num
            if ps-k in freq:
                ans+=freq[ps-k]
            if ps in freq:
                freq[ps]+=1
            else:
                freq[ps]=1
        return ans
        