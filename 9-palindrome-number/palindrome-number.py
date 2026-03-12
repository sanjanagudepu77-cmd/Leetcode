class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        n=x
        rev=0
        while(n>0):
            r=n%10
            rev=rev*10+r
            n=n//10
        if rev==x:
            return True
        else:
            return False
           

        