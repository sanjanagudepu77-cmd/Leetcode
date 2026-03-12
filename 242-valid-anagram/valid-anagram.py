class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        c=[0]*26
        for ch in s:
            c[ord(ch)-ord('a')]+=1
        for ch in t:
            if c[ord(ch)-ord('a')]==0:
                return False
            c[ord(ch)-ord('a')]-=1
        return True


        