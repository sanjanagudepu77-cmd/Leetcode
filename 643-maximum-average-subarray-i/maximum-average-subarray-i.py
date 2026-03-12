class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg=sum(nums[:k])/k
        mavg=avg
        for i in range(k,len(nums)):
           avg=avg+(nums[i]-nums[i-k])/k
           mavg=max(mavg,avg)
        return mavg
        