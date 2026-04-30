class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        es=sum(nums)
        ds=0
        for num in nums:
            while num>0:
                ds=ds+num%10
                num=num//10
        return abs(es-ds)
        