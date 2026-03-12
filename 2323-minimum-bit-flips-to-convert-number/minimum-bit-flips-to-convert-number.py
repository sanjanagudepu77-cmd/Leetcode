'''class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans=start^goal
        res=bin(ans).count("1")
        return res'''
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans=start^goal
        c=0
        while(ans!=0):
            r=ans%2
            if r==1:
                c+=1
            ans=ans//2
        return c

        