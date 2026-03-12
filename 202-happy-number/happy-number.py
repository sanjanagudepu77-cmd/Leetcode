class Solution:
    def isHappy(self, n: int) -> bool:
        def getNextNumber(n):
            total=0
            while n>0:
              d=n%10
              total+=d*d
              n=n//10
            return total
        slow=n
        fast=getNextNumber(n)
        while fast!=1 and slow!=fast:
            slow=getNextNumber(slow)
            fast=getNextNumber(getNextNumber(fast))
        if fast==1:
            return True
        else:
            return False

        