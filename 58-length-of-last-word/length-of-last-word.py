class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        l=len(a)
        return len(a[l-1])
        