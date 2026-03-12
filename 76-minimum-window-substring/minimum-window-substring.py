class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        freq={}
        for c in t:
            if c in freq:
                freq[c]+=1
            else:
                freq[c]=1
        left=0
        ml=float('inf')
        c=0
        start=0
        for r in range(len(s)):
            if s[r] in freq:
                if freq[s[r]]>0:
                    c+=1
                freq[s[r]]-=1
            while(c==len(t)):
                if r-left+1<ml:
                    ml=r-left+1
                    start=left
                if s[left] in freq:
                    freq[s[left]]+=1
                    if freq[s[left]]>0:
                      c-=1
                left+=1
        if ml==float('inf'):
            return ""
        else:
            return s[start:start+ml]

        