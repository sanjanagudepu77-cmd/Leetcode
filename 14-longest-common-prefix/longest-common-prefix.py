class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p=strs[0]
        x=len(p)
        for i in strs[1:]:
            while p!=i[0:x]:
                x-=1
                if x==0:
                    return ""
                p=p[0:x]
        return p
        