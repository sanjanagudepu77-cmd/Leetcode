class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''if not nums:
            return 0
        n=len(nums) #brute
        nums.sort()
        ml=1
        curr=1
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                curr+=1
                ml=max(ml,curr)
            else:
                curr=1
        return ml'''
        ml=0
        nset=set(nums)
        for num in nset:
          if num-1 not in nset:
            curr=num
            length=1
            while curr+1 in nset:
                curr+=1
                length+=1
            ml=max(ml,length)
        return ml



            

