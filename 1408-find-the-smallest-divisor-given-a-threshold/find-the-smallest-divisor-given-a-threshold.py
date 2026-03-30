class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def possible(div):
            sum=0
            for num in nums:
               sum+=math.ceil(num/div)
            return sum<=threshold
        l=1
        h=max(nums)
        ans=-1
        while l<=h:
            mid=(l+h)//2
            if possible(mid):
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans