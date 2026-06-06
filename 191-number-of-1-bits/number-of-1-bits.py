class Solution:
    def hammingWeight(self, n: int) -> int:
        '''count=0
        while n:
            count+=n&1
            n>>=1
        return count'''
        c=0
        while n>1:
            if n%2==1:
                c+=1
            n=n//2
        if n==1:
            c+=1
        return c