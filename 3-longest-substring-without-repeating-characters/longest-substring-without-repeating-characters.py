class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        l=0
        ml=0
        chset=set()
        for r in range(n):
            if s[r] not in chset:
                chset.add(s[r])
                ml=max(ml,r-l+1)
            else:
                while s[r] in chset:
                    chset.remove(s[l])
                    l+=1
                chset.add(s[r])
        return ml
        