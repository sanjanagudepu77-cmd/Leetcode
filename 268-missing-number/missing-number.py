class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''n=len(nums)
        for i in range(0,n+1):
            if i not in nums:
                return i'''
        '''n = len(nums)
        xor_all = 0
        for i in range(n+1):
            xor_all = xor_all ^ i   
        for num in nums:
            xor_all = xor_all ^ num
        return xor_all'''
        n = len(nums)
        total = n * (n + 1) // 2    
        return total - sum(nums)